import sys

board = [list(map(int, input().strip())) for _ in range(9)]

zeros = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            zeros.append((r, c))


def promising_check(r, c, num):
    for k in range(9):
        if board[r][k] == num:
            return 0
        if board[k][c] == num:
            return 0

    for i in range(r // 3 * 3, r // 3 * 3 + 3):
        for j in range(c // 3 * 3, c // 3 * 3 + 3):
            if board[i][j] == num:
                return 0

    return 1


def dfs(depth):
    if depth == len(zeros):
        for r in range(9):
            for c in range(9):
                print(board[r][c], end="")
            print()
        sys.exit()

    r, c = zeros[depth]

    for num in range(1, 10):
        if promising_check(r, c, num):
            board[r][c] = num
            dfs(depth + 1)
            board[r][c] = 0


dfs(0)
