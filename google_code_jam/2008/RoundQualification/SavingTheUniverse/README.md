# Saving the Universe 
[тестовая система](https://codingcompetitions.withgoogle.com/codejam/round/0000000000432b79/000000000043290d)

## Problem
The urban legend goes that if you go to the Google homepage and search for "Google", the universe will implode. We have a secret to share... It is true! Please don't try it, or tell anyone. All right, maybe not. We are just kidding.

The same is not true for a universe far far away. In that universe, if you search on any search engine for that search engine's name, the universe does implode!

To combat this, people came up with an interesting solution. All queries are pooled together. They are passed to a central system that decides which query goes to which search engine. The central system sends a series of queries to one search engine, and can switch to another at any time. Queries must be processed in the order they're received. The central system must never send a query to a search engine whose name matches the query. In order to reduce costs, the number of switches should be minimized.

Your task is to tell us how many times the central system will have to switch between search engines, assuming that we program it optimally.

## Input
The first line of the input file contains the number of cases, **N**. **N** test cases follow.

Each case starts with the number **S** – the number of search engines. The next **S** lines each contain the name of a search engine. Each search engine name is no more than one hundred characters long and contains only uppercase letters, lowercase letters, spaces, and numbers. There will not be two search engines with the same name.

The following line contains a number **Q** – the number of incoming queries. The next **Q** lines will each contain a query. Each query will be the name of a search engine in the case.

## Output
For each input case, you should output:
"Case #**X**: **Y**",
where **X** is the number of the test case and **Y** is the number of search engine switches. Do not count the initial choice of a search engine as a switch.

## Limits
*Time limit*: 30 seconds per test set.
</br>*Memory limit*: 1GB.
</br>0 < **N** ≤ 20

#### Small dataset (Test set 1 - Visible)
2 ≤ **S** ≤ 10
</br>0 ≤ **Q** ≤ 100

#### Large dataset (Test set 2 - Hidden)
2 ≤ **S** ≤ 100
</br>0 ≤ **Q** ≤ 1000

## Sample
| Input        | Output           |
| ------------- |:-------------|
| 2</br>5</br>Yeehaw</br>NSM</br>Dont Ask</br>B9</br>Googol</br>10</br>Yeehaw</br>Yeehaw</br>Googol</br>B9</br>Googol</br>NSM</br>B9</br>NSM</br>Dont Ask</br>Googol</br>5</br>Yeehaw</br>NSM</br>Dont Ask</br>B9</br>Googol</br>7</br>Googol</br>Dont Ask</br>NSM</br>NSM</br>Yeehaw</br>Yeehaw</br>Googol | Case #1: 1</br>Case #2: 0 |