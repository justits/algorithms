if __name__ == '__main__':
    n, m = [int(i) for i in input().split(' ')]
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    max_a = max(a)
    max_b = max(b)
    first_max = a.index(max_a)
    last_max = n - 1 - a[::-1].index(max_a)

    ans_a = sum(a) + max_a * (m - 1)
    ans_b = sum(b) + max_b * (last_max - first_max) + b[0] * first_max + b[m - 1] * (n - 1 - last_max)
    print(ans_a * 1_000_000_000 + ans_b)
