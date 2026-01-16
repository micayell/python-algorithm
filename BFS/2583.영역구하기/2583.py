from collections import deque


def bfs(st_x, st_y):
    queue = deque()
    queue.append((st_x, st_y))
    visited[st_x][st_y] = 1
    demensions = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if not visited[nx][ny] and arr[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                demensions += 1

    return demensions


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N, K = map(int, input().split())

arr = [[0] * (N) for _ in range(M)]
visited = [[0] * (N) for _ in range(M)]

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] += 1

cnt = 0
res = []
for i in range(M):
    for j in range(N):
        if not arr[i][j] and not visited[i][j]:
            demensions = bfs(i, j)
            res.append(demensions)
            cnt += 1

print(cnt)
print(*sorted(res))
