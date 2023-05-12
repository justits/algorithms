def PascalWalk(N):
    skip = 0
    row = 1
    col = 1
    left = True
    while N > 1:
        if N % 2 == 0:
            skip += 1
            print(row, col)
        else:
            for i in range(row):
                print(row, col)
                col = col + (1 if left else -1)
            left = not left
            col = col + (1 if left else -1)

        N //= 2
        row += 1
        if left is False:
            col += 1

    end = min(skip, 3)
    for i in range(row - end):
        print(row, col)
        col = col + (1 if left else -1)

    if skip > 1:
        row -= 1
        col = col + (-1 if left else 0)
        print(row, col)
        if skip != 2:
            col = col + (1 if left else -1)
            print(row, col)
        if skip > 2:
            max_skip = row
            col = col + (1 if left else -1)
            print(row, col)
            for _ in range(max_skip - skip):
                row += 1
                col += 1 if left else 0
                print(row, col)


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        print('Case #{}:'.format(t + 1))
        PascalWalk(N)
