n=int(input())

dx=[-1,1,0,0,-1,-1,1,1] # 상 하 좌 우 좌상 우상 좌하 우하
dy=[0,0,-1,1,-1,1,-1,1]

def Queen(x,y):
    global cnt
    visited[x][y]=1

    for b in range(n):
        for k in range(4):
            nx = x + dx[k]*b
            ny = y + dy[k]*b
            if nx < 0 or ny < 0 or nx >=n or ny >= n:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny]=1

cnt=0
visited=[[0]*n for _ in range(n)]


for i in range(n):
        for j in range(n):
              Queen(i,j)

print(cnt)