def rotate(sticker):
    r, c = len(sticker), len(sticker[0])

    new_sticker = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new_sticker[j][r - i - 1] = sticker[i][j]

    return new_sticker


def can_attach(sticker, x, y):
    r, c = len(sticker), len(sticker[0])

    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and notebook[x + i][y + j] == 1:
                return 0
    return 1


def attach(sticker, x, y):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                notebook[x + i][y + j] = 1


n, m, k = map(int, input().split())
notebook = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]

    attached = 0
    for _ in range(4):  # 4번의 회전 동안 시도
        cur_r, cur_c = len(sticker), len(sticker[0])
        for i in range(n - cur_r + 1):
            for j in range(m - cur_c + 1):
                if can_attach(sticker, i, j):
                    attach(sticker, i, j)
                    attached = 1
                    break
            if attached:
                break
        if attached:
            break

        sticker = rotate(sticker)


res = 0
for row in notebook:
    res += sum(row)

print(res)
