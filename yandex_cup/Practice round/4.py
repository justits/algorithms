def my_ver(n, m):
    ans = n * m
    exp_n, exp_m = 0, 0
    exp, t = 0, 1
    while t < n or t < m:
        t *= 2
        exp += 1
        exp_n = exp if t == n else exp_n
        exp_m = exp if t == m else exp_m

    if n >= m:
        if n > 1:
            add_diff = 1
            for _ in range(exp_n - exp_m + 1):
                for i in range(m):
                    add = 2 * (i + 1) + m * (n - 1)
                    ans += 1 if add * add_diff > n * m else 0
                add_diff *= 2
            ans += 2 * exp_m - 1
    else:
        add_diff = 1
        for _ in range(exp_m - exp_n):
            for i in range(n):
                add = 2 * i * m + m + 1
                ans += 1 if add * add_diff > n * m else 0
            add_diff *= 2
        ans += 2 * exp_n
    return ans


n, m = [int(i) for i in input().split(' ')]
print(my_ver(n, m))
