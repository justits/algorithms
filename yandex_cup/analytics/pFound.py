import pandas as pd
import os

OPEN_TASK_DIR = 'data/open_task'
HIDDEN_TASK_DIR = 'data/hidden_task'
DIR = HIDDEN_TASK_DIR
P_BREAK = 0.15


# Calculate pFound metric
def calculate_pfound(group):
    pFound = 0
    pLook = 1
    for pRel in group.rating.head(10):
        pFound += pLook * pRel
        pLook = pLook * (1 - pRel) * (1 - P_BREAK)
    return pFound


if __name__ == "__main__":
    # Load data
    qid_query = pd.read_csv(os.path.join(DIR, 'qid_query.tsv'), sep='\t', names=['query_id', 'query'])
    qid_url_rating = pd.read_csv(os.path.join(DIR, 'qid_url_rating.tsv'), sep='\t', names=['query_id', 'url', 'rating'])
    hostid_url = pd.read_csv(os.path.join(DIR, 'hostid_url.tsv'), sep='\t', names=['host_id', 'url'])

    # Find query with maximum pFound
    qid_max_pfound = qid_url_rating \
        .merge(hostid_url, on='url') \
        .sort_values(['query_id', 'rating'], ascending=[True, False]) \
        .drop_duplicates(['query_id', 'host_id']) \
        .groupby('query_id') \
        .apply(calculate_pfound) \
        .idxmax()

    # Output the query with maximum pFound
    max_pfound_query = qid_query[qid_query.query_id == qid_max_pfound]
    print(max_pfound_query)
