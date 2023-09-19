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