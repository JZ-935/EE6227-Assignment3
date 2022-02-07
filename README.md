# EE6227 Assignment3 - Simple Genetic Algorithm
> this is a `readme.md` file that introduces the SGA

## I. Steps to start running SGA
1. double click the `SimpleGA.exe` file 
2. there are 2 inputs that are required from user, one is `POPULATION_SIZE`, the other is `N`(chessboard size)

## II. Advanced modification of `SimpleGA.py`
1. make sure you have installed python(3.9) and open the file with *spyder* or *pycharm*

## III. Basic thought of the SGA
>The basic thought of this algorithm is based on the reference book: *Introduction to Evolutionary Computing*, chapter 3-4-1 The Eight-Queens problem
>
>This chapter introduce 2 operation: 
>1. "Cut&fill" **Crossover**
>2. "Swap" **Mutation**

### The details of the two operations are shown below: 
#### "Cut&fill" **Crossover operation** 
1. Select a random position, the crossover point, i $\in$ {1, 2, 3, 4, 5, 6, 7} 
2. Cut both parents into two segments at this position 
3. Copy the first segment of parent 1 into child 1 and the first segment ofparent 2intochild 2 
4. Scan parent 2 from left to right and fill the second segment of child 1 with values from parent 2, skipping those that it already contains 
5. Do the same for parent 1 and child 2 

#### "Swap" **Mutation operation** 
1. Randomly choose 2 position and swap thier values 
