import numpy as np


def get_prefix(patterns):
    P = ['*']
    for pattern in patterns:
        index = 0
        while index < len(pattern) and pattern[index] != '*':
            if index < (len(P[:-1]) if P[-1] == '*' else len(P)):
                if pattern[index] == P[index]:
                    index += 1
                else:
                    return None
            elif P[-1] == '*':
                P = P[:-1] + [pattern[index]] + (['*'] if index != len(pattern) - 1 else [])
                index += 1
            else:
                return None
    return P


def get_insides(patterns):
    inside = []
    for pattern in patterns:
        indexes = np.where(np.array(pattern) == '*')[0]
        if len(indexes) > 1:
            inside += [''.join(pattern[indexes[i] + 1:indexes[i + 1]]) for i in range(len(indexes) - 1)]
    return inside


def PatternMatching():
    N = int(input())
    patterns = [list(input()) for _ in range(N)]
    patterns_reverse = [pattern[::-1] for pattern in patterns]
    P = get_prefix(patterns)
    S = get_prefix(patterns_reverse)

    if S is None or P is None:
        result = ['*']
    else:
        inside = get_insides(patterns)
        if P[-1] != '*':
            result = P
        elif S[-1] != '*':
            result = S[::-1]
        else:
            result = P[:-1] + inside + S[:-1][::-1]
    return result


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        result = PatternMatching()
        print('Case #{}: {}'.format(t, ''.join(result)))
