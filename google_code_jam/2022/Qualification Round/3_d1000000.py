T = int(input())
for t in range(T):
    N = int(input())
    dS = [int(i) for i in input().split(' ')]
    dS.sort()
    ans = 1
    for side in dS[1:]:
        if side > ans:
            ans += 1
    print(f'Case #{t +1}:', ans)
