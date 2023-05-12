T = int(input())
for t in range(T):
    N = int(input())
    fun = [int(i) for i in input().split(' ')]
    parent = [int(i) for i in input().split(' ')]
    connection = [[] for _ in range(N)]
    for i in range(N):
        if parent[i] > 0:
            connection[parent[i] - 1].append(i)
    ans = 0
    for i in range(N - 1, -1, -1):
        if len(connection[i]) > 0:
            f_i = [fun[p] for p in connection[i]]
            fun[i] = max(fun[i], min(f_i))
            ans += sum(f_i) - min(f_i)
        if parent[i] == 0:
            ans += fun[i]
    print(f'Case #{t + 1}:', ans)
    