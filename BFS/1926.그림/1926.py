from collections import deque

# arr[dx][dy]
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def query(x, y):
    global temp_dimensions
    temp_dimensions=0
    queue = deque()
    queue.append((x, y))
    temp_dimensions+=1
    visited[x][y]=1
    

    while queue:
        
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if visited[nx][ny]==0 and picture[nx][ny]==1:
                queue.append((nx,ny))
                visited[nx][ny]=1
                temp_dimensions+=1


n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dimensions=0
temp_dimensions=0

cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and picture[i][j] == 1:
            query(i, j)
            cnt += 1
            if dimensions < temp_dimensions:
                dimensions = temp_dimensions


print(cnt)
print(dimensions)