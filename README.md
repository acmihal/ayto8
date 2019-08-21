# AYTO Season 8 Constraint Solver

This program finds the feasible matches for the 'Are You The One: Season 8' reality TV dating show.

## Running the Solver

```bash
pip install -r requirements.txt
python ayto8.py
```

## Additional Information

As new information is revealed in each episode, add new lines to the truthBooths and matchingCeremonies functions.

## References

A constraint satisfaction formulation relevant to previous seasons of the show
was written by [Natalia Summerville](https://blogs.sas.com/content/operations/2018/08/14/are-you-the-one/).
This formulation generalizes the problem to non-monosexuality.
The optimal strategies discussed in the previous work are not considered here.

This program uses the [Z3 Theorem Prover](https://rise4fun.com/z3).

## License and Citation

ayto8.py is released under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Example Output

```
number of solutions if the match is true / number of solutions if the match is false
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -        11/0       -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -        2/9        -        2/9       2/9       2/9        -        1/10      2/9    amber
     basit                                  -         -         -         -        11/0       -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -        10/1       -        1/10       -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -        11/0       -         -     jasmine
     jenna                                                                          -         -         -        1/10       -         -         -        10/1       -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -        3/8       3/8       1/10       -         -        2/9    justin
       kai                                                                                                        -         -         -         -         -        1/10   kai
      kari                                                                                                                  -        3/8        -         -        2/9    kari
     kylie                                                                                                                           3/8        -         -        2/9    kylie
       max                                                                                                                                      -         -        2/9    max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Testing match justin+max: result=sat
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         -         -         -         -         X         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         -         -         X         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         X         -         -         -         -         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         -         -         X         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         X     kai
      kari                                                                                                                  -         -         -         -         -     kari
     kylie                                                                                                                            -         -         -         -     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 1
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         -         -         -         -         X         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         -         -         X         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         X         -         -         -         -         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         -         -         X         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         X     kai
      kari                                                                                                                  -         -         -         -         -     kari
     kylie                                                                                                                            -         -         -         -     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 2
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         X         -         -         -         -         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         -         X         -         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         -         -         -         -     kari
     kylie                                                                                                                            -         -         -         -     kylie
       max                                                                                                                                      -         -         X     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 3
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         -         X         -         -         -         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         X         -         -         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         -         -         -         -     kari
     kylie                                                                                                                            -         -         -         -     kylie
       max                                                                                                                                      -         -         X     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 4
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         X         -         -         -         -         -         -         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         -         -         -         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         X         -         -         -     kari
     kylie                                                                                                                            -         -         -         X     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 5
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         -         -         X         -         -         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         X         -         -         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         -         -         -         -     kari
     kylie                                                                                                                            -         -         -         X     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 6
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         -         -         -         -         -         X     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         -         X         -         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         X         -         -         -     kari
     kylie                                                                                                                            -         -         -         -     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 7
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         -         -         -         -         -         X     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         X         -         -         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         -         -         -         -     kari
     kylie                                                                                                                            X         -         -         -     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 8
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         -         X         -         -         -         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         -         -         -         -         -         X     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         X         -         -         -     kari
     kylie                                                                                                                            -         -         -         -     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 9
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         X         -         -         -         -         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         -         -         -         -         -         X     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         -         -         -         -     kari
     kylie                                                                                                                            X         -         -         -     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 10
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         -         -         -         -         X         -         -         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         -         X         -         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         -         -         -         X     kari
     kylie                                                                                                                            -         -         -         -     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
Solution 11
            aasha     amber     basit    brandon    danny    jasmine    jenna    jonathan   justin     kai       kari     kylie      max       nour     paige      remy   
     aasha              -         -         X         -         -         -         -         -         -         -         -         -         -         -         -     aasha
     amber                        -         -         -         -         -         -         X         -         -         -         -         -         -         -     amber
     basit                                  -         -         -         -         X         -         -         -         -         -         -         -         -     basit
   brandon                                            -         -         -         -         -         -         -         -         -         -         -         -     brandon
     danny                                                      -         -         -         -         X         -         -         -         -         -         -     danny
   jasmine                                                                -         -         -         -         -         -         -         X         -         -     jasmine
     jenna                                                                          -         -         -         -         -         -         -         X         -     jenna
  jonathan                                                                                    -         -         -         -         -         -         -         -     jonathan
    justin                                                                                              -         -         -         -         -         -         -     justin
       kai                                                                                                        -         -         -         -         -         -     kai
      kari                                                                                                                  -         -         -         -         X     kari
     kylie                                                                                                                            X         -         -         -     kylie
       max                                                                                                                                      -         -         -     max
      nour                                                                                                                                                -         -     nour
     paige                                                                                                                                                          -     paige
      remy                                                                                                                                                                remy
```
