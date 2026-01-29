from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = [[-1] * m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans[i][j] = 0
        elif arr[i][j] == 2:
            q.append((i, j))
            ans[i][j] = 0

while q:
    x, y = q.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if arr[nx][ny] == 0:
            continue
        if arr[nx][ny] == 1 and ans[nx][ny] == -1:
            ans[nx][ny] = ans[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    print(*ans[i])
