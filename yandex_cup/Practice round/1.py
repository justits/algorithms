s1 = input().replace('zero', '0').replace('one', '1')
s2 = input().replace('zero', '0').replace('one', '1')

if len(s1) < len(s2):
    print('<')
elif len(s1) > len(s2):
    print('>')
else:
    if s1 < s2:
        print('<')
    elif s1 == s2:
        print('=')
    else:
        print('>')