# class Plitka:


k = int(input())
el = {}
for _ in range(k):
    s = input() + input()[::-1]
    s = min([s, s[-1:] + s[:-1], s[-2:] + s[:-2], s[-3:] + s[:-3]])
    if s not in el:
        el[s] = 0
    el[s] += 1

n, m = [int(i) for i in input().split()]
ans = True
for _ in range(n // 2):
    s1 = input()
    s2 = input()
    for i in range(m // 2):
        s = s1[(2 * i):(2 * i + 2)] + s2[(2 * i):(2 * i + 2)][::-1]
        s = min([s, s[-1:] + s[:-1], s[-2:] + s[:-2], s[-3:] + s[:-3]])
        if s not in el:
            ans = False
            break
        el[s] -= 1
        if el[s] < 0:
            ans = False
            break
print('Yes' if ans else 'No')