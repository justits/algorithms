s = input()

alphbeth = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ans = ''
find = False
pos = 0
ex = 1
while len(s) > 0:
    s_even = s[::2]
    s_odd = s[1::2]
    if len(s_even) and s_even[0] in alphbeth and s_even == ''.join(s_even[0] * len(s_even)):
        ans += s_even[0]
        alphbeth.remove(s_even[0])
        s = s_odd
        pos = pos if find else ex
        find = True
    elif len(s_odd) and s_odd[0] in alphbeth and s_odd == ''.join(s_odd[0] * len(s_odd)):
        ans += s_odd[0]
        alphbeth.remove(s_odd[0])
        pos = pos + ex if find else pos
        s = s_even
    else:
        ans = ''
        break
    ex *= 2

if len(ans) > 0:
    ans += ''.join(alphbeth)
    print(ans)
    print(pos)
else:
    print('No solution')
