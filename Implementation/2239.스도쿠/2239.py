board = [list(map(int, input().strip())) for _ in range(9)]
# print(board)

zeros = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            zeros.append((r, c))
# print(zeros)


def promising_check(r, c, num):
    flag = 1
    for k in range(9):
        if board[r][k] == num:
            flag = 0
        if board[k][c] == num:
            flag = 0

    for i in range(r // 3 * 3, r // 3 * 3 + 3):
        for j in range(c // 3 * 3, c // 3 * 3 + 3):
            if board[i][j] == num:
                flag = 0

    return flag


def dfs(depth):
    if depth == len(zeros):
        for r in range(9):
            for c in range(9):
                print(board[r][c], end="")
            print()
        return

    r, c = zeros[depth]

    for num in range(1, 10):
        if promising_check(r, c, num):
            board[r][c] = num
            dfs(depth + 1)
            board[r][c] = 0


dfs(0)
