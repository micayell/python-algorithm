N, M = map(int, input().split())
pan = [list(input()) for _ in range(N)]


def find_paint(r, c):
    drawl = 0
    for i in range(r, r + 8):
        for j in range(c, c + 8):
            if (i + j) % 2 == 0:
                if pan[i][j] == "B":
                    drawl += 1
            else:
                if pan[i][j] == "W":
                    drawl += 1

    total = min(drawl, 64 - drawl)
    return total


cnt = 64
for i in range(N - 7):
    for j in range(M - 7):
        temp = find_paint(i, j)
        if cnt > temp:
            cnt = temp

print(cnt)
