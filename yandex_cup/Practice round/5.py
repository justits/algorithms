n, m = [int(i) for i in input().split(' ')]
board = [0] * n
n_0 = m * n
for i in range(n):
    board[i] = [int(j) for j in input()]
    n_0 -= sum(board[i])


def fun(line, n_0_sub, m_sub):
    n_sub = n - line
    left_sub = n_0_sub // n_sub
    v = [sum(board[line][:i + 1]) + fun(line + 1, n_0_sub - i - 1, i + 1) for i in range(left_sub, m_sub) if i < n_0_sub]
    return min(v) if len(v) > 0 else 0


left = n_0 // n

v = [sum(board[0][:(i + 1)]) + fun(1, n_0 - i - 1, m) for i in range(left, i + 1) if i < n_0]
ans = min(v) if len(v) > 0 else 0

print(ans)


