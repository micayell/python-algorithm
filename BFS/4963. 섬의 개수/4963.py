from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1] # 상 하 좌 우 좌상 좌하 우상 우하
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def find_islands(x,y):
    global data
    queue = deque([(x,y)])
    data[x][y] = 0

    while queue:
        x,y= queue.popleft()
        for k in range(8):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or ny<0 or nx >=h or ny >=w:
                continue
            if data[nx][ny] == 0:
                continue
            queue.append((nx,ny))
            data[nx][ny] = 0


while(True):
    w,h = map(int, input().split())
    if (w,h) == (0,0):
        break
    data = [list(map(int,input().split())) for _ in range(h)]
    # print(data)
    result = 0

    for x in range(h):
        for y in range(w):
            if data[x][y] == 1:
                find_islands(x,y)
                result +=1

    print(result)