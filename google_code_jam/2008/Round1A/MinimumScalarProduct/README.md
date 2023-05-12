# Minimum Scalar Product 
[тестовая система](https://codingcompetitions.withgoogle.com/codejam/round/00000000004330f6/0000000000432f33)

## Problem
You are given two vectors v<sub>1</sub> = (x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub>) and v<sub>2</sub> = (y<sub>1</sub>, y<sub>2</sub>, ..., y<sub>n</sub>). The scalar product of these vectors is a single number, calculated as x<sub>1</sub>y<sub>1</sub> + x<sub>2</sub>y<sub>2</sub> + ... + x<sub>n</sub>y<sub>n</sub>.

Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product.

## Input
The first line of the input file contains integer number **T** - the number of test cases. For each test case, the first line contains integer number **n**. The next two lines contain **n** integers each, giving the coordinates of v<sub>1</sub> and v<sub>2</sub> respectively.

## Output
For each test case, output a line
"Case #**X**: **Y**",
where **X** is the test case number, starting from 1, and **Y** is the minimum scalar product of all permutations of the two given vectors.

## Limits
*Time limit:* 30 seconds per test set.
</br>*Memory limit:* 1GB.

#### Small dataset (Test set 1 - Visible)
**T** = 1000
</br>1 ≤ **n** ≤ 8
</br>-1000 ≤ **x<sub>i</sub>**, **y<sub>i</sub>** ≤ 1000

#### Large dataset (Test set 2 - Hidden)
**T** = 10
</br>100 ≤ **n** ≤ 800
</br>-100000 ≤ **x<sub>i</sub>**, **y<sub>i</sub>** ≤ 100000

## Sample
| Input        | Output           |
| ------------- |:-------------|
| 2</br>3</br>1 3 -5</br>-2 4 1</br>5</br>1 2 3 4 5</br>1 0 1 0 1 | Case #1: -25</br>Case #2: 6 |