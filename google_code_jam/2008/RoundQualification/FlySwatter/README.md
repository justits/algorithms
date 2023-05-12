# Fly Swatter
[тестовая система](https://codingcompetitions.withgoogle.com/codejam/round/0000000000432b79/0000000000432f32)

## Problem
What are your chances of hitting a fly with a tennis racquet?

To start with, ignore the racquet's handle. Assume the racquet is a perfect ring, of outer radius **R** and thickness **t** (so the inner radius of the ring is **R−t**).

The ring is covered with horizontal and vertical strings. Each string is a cylinder of radius **r**. Each string is a chord of the ring (a straight line connecting two points of the circle). There is a gap of length **g** between neighbouring strings. The strings are symmetric with respect to the center of the racquet i.e. there is a pair of strings whose centers meet at the center of the ring.

The fly is a sphere of radius **f**. Assume that the racquet is moving in a straight line perpendicular to the plane of the ring. Assume also that the fly's center is inside the outer radius of the racquet and is equally likely to be anywhere within that radius. Any overlap between the fly and the racquet (the ring or a string) counts as a hit.

![alt text](https://codejam.googleapis.com/dashboard/get_file/AQj_6U0mWZ1I4-zFNJrEsKwit3HPdqMkHwEg2d9mTCEtOjcsJJfZ35TG9unV6w/test2.png)

## Input
One line containing an integer **N**, the number of test cases in the input file.

The next **N** lines will each contain the numbers **f**, **R**, **t**, **r** and **g** separated by exactly one space. Also the numbers will have exactly 6 digits after the decimal point.

## Output
**N** lines, each of the form 
"Case #**X**: **Y**", 
where **X** is the number of the test case and **Y** is the probability of hitting the fly with a piece of the racquet.

Answers with a relative or absolute error of at most 10<sup>-6</sup> will be considered correct.

## Limits
*Time limit*: 60 seconds per test set.
</br>*Memory limit*: 1GB.
</br>**f**, **R**, **t**, **r** and **g** will be positive and smaller or equal to 10000.
</br>**t** < **R**
</br>**f** < **R**
</br>**r** < **R**

#### Small dataset (Test set 1 - Visible)
1 ≤ **N** ≤ 30
The total number of strings will be at most 60 (so at most 30 in each direction).

#### Large dataset (Test set 2 - Hidden)
1 ≤ **N** ≤ 100
The total number of strings will be at most 2000 (so at most 1000 in each direction).

## Sample
| Input        | Output           |
| ------------- |:-------------|
| 5<br/>0.250000 1.000000 0.100000 0.010000 0.500000<br/>0.250000 1.000000 0.100000 0.010000 0.900000<br/>0.000010 10000.000000 0.000010 0.000010 1000.000000<br/>0.400000 10000.000000 0.000010 0.000010 700.000000<br/>1.000000 100.000000 1.000000 1.000000 10.000000      | Case #1: 1.000000<br/>Case #2: 0.910015<br/>Case #3: 0.000000<br/>Case #4: 0.002371<br/>Case #5: 0.573972 |