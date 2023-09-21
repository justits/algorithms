## calculate pFound
The archive contains three text files:

- qid_query.tsv — query id and query text;
- qid_url_rating.tsv – query id, document URL, relevance of the document to the query;
- hostid_url.tsv — host id and document URL.

Output the **query text** with the maximum value of the **pFound** metric calculated from the top 10 documents.

If there are several documents with the same host id for the query, leave only the most relevant document (and if several documents are as relevant as possible, choose any one).

**Formula for calculating pFound:**

```math
\sum_{i=1}^{10} pLook[i] \cdot pRel[i]
```
```math
pLook[1] = 1
```
```math
pLook[i] = pLook[i-1] \cdot (1-pRel[i-1]) \cdot (1-pBreak)
```
```math
pBreak = 0.15
```

## single-elimination tournament

While Mary was on vacation, her colleagues organized a chess tournament according to the Olympic system. 
During the rest, Mary did not pay much attention to this idea, so she can barely remember who played with whom. 
Suddenly Mary came up with the idea that it would be nice to bring a souvenir from vacation to the winner of the tournament.

Mary doesn't know who won the final, but she can easily figure out who played in it, if only she remembered the playing pairs correctly. 
Help her check if this is the case and identify possible candidates for winners.


**Input:**
The first line contains an integer n $3 \leqslant n \leqslant 2^{16} - 1, n = 2^k - 1$ — the number of past games. 

In the next n lines — two surnames of the players separated by a space. 
The surnames of the players are different. 
All surnames are unique, there are no namesakes among colleagues.

**Output:**
Output **NO SOLUTION** if Mary has memorized the games incorrectly and it is impossible to get a Single-elimination tournament using this grid. 
If a tournament grid is possible, print two names of candidates for the first place in one line.

more about [Single-elimination tournament](https://en.wikipedia.org/wiki/Single-elimination_tournament)


## theater season

The international ticket sales service decided to sum up the results of the theater season. 
As one of the metrics, the project manager wants to count the number of users who bought tickets to different performances.

When buying a ticket, the user specifies his phone number. 
It is necessary to find the performance with the largest number of unique phone numbers. 
And count the number of corresponding unique phone numbers.

