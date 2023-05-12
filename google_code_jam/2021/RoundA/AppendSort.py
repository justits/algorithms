import numpy as np


def fun():
    N = int(input())
    X = input().split(' ')
    X_int = np.array([int(x) for x in X])
    X_len = np.array([len(x) for x in X])
    result = 0
    for i in range(1, N):
        if X_int[i] <= X_int[i - 1]:
            if X_len[i] == X_len[i - 1]:
                result += 1
                X_int[i] *= 10
                X_len[i] += 1
            elif X_len[i] < X_len[i - 1]:
                diff = X_len[i - 1] - X_len[i]
                result += diff
                X_int[i] *= int('1' + '0' * diff)
                X_len[i] += diff

                if X_int[i] <= X_int[i - 1]:
                    if X_int[i - 1] - X_int[i] >= int('9' * diff):
                        result += 1
                        X_int[i] *= 10
                        X_len[i] += 1
                    else:
                        X_int[i] = X_int[i - 1] + 1
    return result


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print('Case #{}: {}'.format(t + 1, fun()))
