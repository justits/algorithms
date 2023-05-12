import numpy as np


def saving_the_universe():
    S = int(input())
    search_engines = {input(): i for i in range(S)}
    Q = int(input())
    queries = [search_engines[input()] for _ in range(Q)]
    switch = 0
    block = np.array([1] * S)
    for i in range(Q):
        block[queries[i]] = 0
        if sum(block) == 0:
            switch += 1
            block = np.array([1] * S)
            block[queries[i]] = 0
    return switch

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        result = saving_the_universe()
        print('Case  #{}: {}'.format(t + 1, result))
