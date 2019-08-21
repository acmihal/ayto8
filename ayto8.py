# AYTO Season 8 Constraint Solver
# Author: Andrew Mihal <andrew@acmihal.com>
# Date: 14 August 2019
# License: CC BY-NC-SA 4.0 International

# This utility uses the `Z3 theorem prover <https://rise4fun.com/z3>`_.
from z3 import Bool, And, Not, PbEq, Solver, sat

# The number of ways to group N persons into couples is N! / ( (N/2)! * 2^(N/2) )
# For N=16, the result is 2,027,025.

# The names of the contestants.
Contestants = sorted(set(['nour','amber','kari','kylie','max','justin','basit','jonathan','aasha','paige','remy','brandon','jasmine','jenna','kai','danny']))


# Return a Boolean variable that is True when contestants a and b are a match, and False when they are a no-match.
def perfectMatch(a, b):
    assert a in Contestants and b in Contestants
    return Bool('+'.join(sorted([a, b])))


# Return a constraint that each contestant must match exactly one other contestant.
# Singles, throuples or bigger poly groups are not allowed to go to the matching ceremony as a "couple".
def oneMatchPerContestant():
    return And([PbEq([(perfectMatch(a, b), 1) for b in Contestants if b != a], 1) for a in Contestants])


# Constraints provided by the Truth Booth.
def truthBooths():
    return And([Not(perfectMatch('nour', 'justin')),
                Not(perfectMatch('remy', 'brandon')),
                Not(perfectMatch('kai', 'jenna')),
                Not(perfectMatch('danny', 'jenna')),
                Not(perfectMatch('kari', 'kylie')),
                    perfectMatch('aasha', 'brandon'),
                    #perfectMatch('basit', 'jonathan'),
              ])


# Returns a constraint that exactly 'count' of the couples in 'a' are matches.
def beamConstraint(count, a):
    assert len(a) == (len(Contestants) / 2)
    assert Contestants == sorted([item for sublist in a for item in sublist])
    return PbEq([(perfectMatch(*c), 1) for c in a], count)


# Constraints provided by the Matching Ceremonies.
def matchingCeremonies():
    return And([beamConstraint(2, [('nour', 'amber'), ('kari', 'kylie'), ('max', 'justin'), ('basit', 'jonathan'), ('aasha', 'paige'), ('remy', 'brandon'), ('jasmine', 'jenna'), ('kai', 'danny')]),
                beamConstraint(2, [('nour', 'amber'), ('kari', 'kylie'), ('max', 'paige'), ('basit', 'jonathan'), ('aasha', 'brandon'), ('remy', 'danny'), ('jasmine', 'justin'), ('kai', 'jenna')]),
                beamConstraint(2, [('jenna', 'justin'), ('kari', 'kylie'), ('max', 'aasha'), ('basit', 'remy'), ('jonathan', 'brandon'), ('paige', 'amber'), ('jasmine', 'nour'), ('kai', 'danny')]),
                beamConstraint(1, [('nour', 'amber'), ('kari', 'kai'), ('max', 'justin'), ('basit', 'danny'), ('aasha', 'remy'), ('paige', 'jenna'), ('jasmine', 'brandon'), ('kylie', 'jonathan')]),
                beamConstraint(0, [('nour', 'amber'), ('kari', 'danny'), ('max', 'brandon'), ('basit', 'remy'), ('aasha', 'kai'), ('jonathan', 'justin'), ('jasmine', 'paige'), ('kylie', 'jenna')]),
                beamConstraint(3, [('nour', 'remy'), ('kari', 'paige'), ('max', 'justin'), ('basit', 'jonathan'), ('aasha', 'brandon'), ('amber', 'jenna'), ('jasmine', 'kylie'), ('kai', 'danny')]),
              ])


# Print a matrix of pairings using the given functor.
def printMatrix(functor):
    # column width
    ts = max([len(c) for c in Contestants]) + 2

    # header row
    print(' ' * ts + ''.join([c.center(ts) for c in Contestants]))

    for i, ci in enumerate(Contestants):
        # heading column
        print(ci.rjust(ts), end='')

        # blank spaces for the lower triangle of the matrix
        print(' ' * ts * (i + 1), end='')

        for cj in Contestants[i+1:]:
            print(functor(ci, cj).center(ts), end='')

        # additional heading column on the right
        print(ci)


# This functor prints whether contestants i and j are matched / not-matched under the given model.
class ModelFunctor(object):
    def __init__(self, model):
        self.model = model

    def __call__(self, i, j):
        if self.model[perfectMatch(i, j)]:
            return 'X'
        else:
            return '-'


# This functor prints the number of solutions that are possible
# when contestants i and j are matched / not-matched.
class CountSolutionsFunctor(object):
    def __init__(self, solver, initial_assumptions=[]):
        self.solver = solver
        self.initial_assumptions = initial_assumptions

    def __call__(self, i, j):
        solutions_if_true = self.__count_solutions(perfectMatch(i, j))
        if solutions_if_true == 0:
            return '-'
        solutions_if_false = self.__count_solutions(Not(perfectMatch(i, j)))
        return '{}/{}'.format(solutions_if_true, solutions_if_false)

    def __count_solutions(self, a):
        solutions = 0
        assumptions = self.initial_assumptions + [a]
        while self.solver.check(assumptions) == sat:
            solutions += 1
            model = self.solver.model()
            assumptions.append(Not(And([x() == model[x] for x in model])))
        return solutions


# Try matching contestants i and j and print a full solution if the match is feasible.
def testMatch(s, i, j):
    v = perfectMatch(i, j)
    result = s.check(v)
    print("Testing match {}: result={}".format(v, str(result)))
    if result == sat:
        printMatrix(ModelFunctor(s.model()))


if __name__ == '__main__':
    s = Solver()

    # Each contestant has to select one match.
    s.add(oneMatchPerContestant())

    # Add the additional information provided by the truth booths and matching ceremonies.
    s.add(truthBooths())
    s.add(matchingCeremonies())

    # Count how many solutions are possible under each possible match / no-match.
    print("number of solutions if the match is true / number of solutions if the match is false")
    printMatrix(CountSolutionsFunctor(s))

    # Test if a match is possible, and print a complete solution if it is.
    testMatch(s, 'max', 'justin') # Andrew's guess

    # Print all solutions.
    solutions = 0
    assumptions = []
    while s.check(assumptions) == sat:
        solutions += 1
        print('Solution {}'.format(solutions))
        model = s.model()
        printMatrix(ModelFunctor(model))
        assumptions.append(Not(And([x() == model[x] for x in model])))


