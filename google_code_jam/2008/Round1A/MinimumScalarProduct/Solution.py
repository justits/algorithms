import numpy as np


def minimum_scalar_product():
    n = int(input())
    v1 = np.sort(np.array([int(i) for i in input().split(' ')]))
    v2 = np.sort(np.array([int(i) for i in input().split(' ')]))[::-1]
    return (v1 * v2).sum()

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        result = minimum_scalar_product()
        print('Case  #{}: {}'.format(t + 1, result))
