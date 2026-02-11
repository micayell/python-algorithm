import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


# 시계 방향 90도 회전
def rotate_90(board):
    new_board = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_board[c][N - 1 - r] = board[r][c]
    return new_board


def move_left(board):
    new_board = [[0] * N for _ in range(N)]

    for i in range(N):
        nums = [x for x in board[i] if x != 0]

        merged = []
        skip = False
        for j in range(len(nums)):
            if skip:
                skip = False
                continue

            if j + 1 < len(nums) and nums[j] == nums[j + 1]:
                merged.append(nums[j] * 2)
                skip = True
            else:
                merged.append(nums[j])

            for j in range(len(merged)):
                new_board[i][j] = merged[j]
    # print(new_board)
    return new_board


def dfs(board, depth):
    global answer

    if depth == 5:
        # print(board)
        for row in board:
            answer = max(answer, max(row))
        return

    temp_board = deepcopy(board)

    for _ in range(4):
        moved_board = move_left(temp_board)
        dfs(moved_board, depth + 1)
        temp_board = rotate_90(temp_board)


answer = 0
dfs(board, 0)
print(answer)
