import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
hcnt = 0
bcnt = 0


def solve(N, r, c):
    global hcnt, bcnt
    color = paper[r][c]

    for i in range(r, r + N):
        for j in range(c, c + N):
            if paper[i][j] != color:
                half = N // 2
                solve(half, r, c)
                solve(half, r, c + half)
                solve(half, r + half, c)
                solve(half, r + half, c + half)
                return

    if color == 0:
        hcnt += 1
    elif color == 1:
        bcnt += 1


solve(N, 0, 0)
print(hcnt)
print(bcnt)
