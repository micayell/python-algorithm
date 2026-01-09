import copy

n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= map[i][j] <= 5:
            cctv.append((i, j, map[i][j]))

# 상우하좌
# arr[dx][dy]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv 1,2,3,4,5 방향설정
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]],
]


def fill(cur_map, mm, x, y):
    for i in mm:
        nx, ny = x, y

        while 1:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or cur_map[nx][ny] == 6:
                break

            if cur_map[nx][ny] == 0:
                cur_map[nx][ny] = "#"


def dfs(level, cur_map):
    global min_value

    if level == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += cur_map[i].count(0)
        min_value = min(min_value, cnt)
        return

    x, y, cctv_type = cctv[level]

    for mm in mode[cctv_type]:
        temp = copy.deepcopy(cur_map)
        fill(temp, mm, x, y)
        dfs(level + 1, temp)


min_value = 21e8

dfs(0, map)
print(min_value)
