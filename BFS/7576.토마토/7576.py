from collections import deque

M, N = map(int, input().split())  # col, row
box = [list(map(int, input().split())) for _ in range(N)]

# 상우하좌, arr[dx][dy]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


queue = deque()

found = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
        elif box[i][j] == 0:
            found = 1

if not found:
    print(0)

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if box[nx][ny] == -1:
            continue
        if box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append((nx, ny))

flag = 1
day = -21e8
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            flag = 0
        if day < box[i][j]:
            day = box[i][j]

if found and flag:
    print(day - 1)

elif found and flag == 0:
    print(-1)
