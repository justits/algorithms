T = int(input())
for t in range(T):
    R, C = map(int, input().split(' '))
    print(f'Case #{t + 1}:')
    print('..+' + '-+' * (C - 1))
    for i in range(R):
        print(('.' if i == 0 else '|') + '.|' * C)
        print('+' + '-+' * C)