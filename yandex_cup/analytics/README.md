## calculate pFound
The archive contains three text files:

- qid_query.tsv — request id and request text;
- qid_url_rating.tsv – request id, document URL, relevance of the document to the request;
- hostid_url.tsv — host id and document URL.

Output the **request text** with the maximum value of the **pFound** metric calculated from the top 10 documents.

If there are several documents with the same host id for the request, leave only the most relevant document (and if several documents are as relevant as possible, choose any one).

**Formula for calculating pFound:**

```math
e^{i\pi} + 1 = 0
```