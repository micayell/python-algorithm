from collections import deque

# arr[dx][dy]
# 상,우,하,좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
T = int(input())


def find(x, y):
    global visited
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny] == 0 and bat[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = 1


for _ in range(T):
    M, N, K = map(
        int, input().split()
    )  # 배추밭의 가로 길이, 세로길이, 배추가 심어져 있는 위치의 개수

    bat = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        bat[x][y] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and bat[i][j] == 1:
                find(i, j)
                cnt += 1

    print(cnt)
