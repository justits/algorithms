NEED_VALUE = 1_000_000

T = int(input())
for t in range(T):
    color = [NEED_VALUE] * 4
    for _ in range(3):
        current_print = map(int, input().split(' '))
        color = [min(i, j)for i, j in zip(current_print, color)]

    if sum(color) < NEED_VALUE:
        print(f'Case #{t + 1}: IMPOSSIBLE')
    else:
        diff = sum(color) - NEED_VALUE
        for i in range(4):
            color[i], diff = color[i] - min(color[i], diff), diff - min(color[i], diff)
        print(f'Case #{t + 1}:', ' '.join(map(str, color)))
