from collections import deque

N, M = map(int, input().split())
pan = [input() for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def find_paint_bfs(start_x, start_y, start_color):
    """
    (start_x, start_y)에서 시작하여 start_color('W' 또는 'B')로 
    시작하는 8x8 체스판을 만들 때 필요한 최소 페인트 횟수 계산
    """
    q = deque([(start_x, start_y, start_color)])
    visited = [[False] * 8 for _ in range(8)]
    visited[0][0] = True
    
    count = 0
    # 시작점의 색이 정해진 색과 다르면 칠해야 함
    if pan[start_x][start_y] != start_color:
        count += 1
        
    while q:
        curr_x, curr_y, curr_color = q.popleft()
        
        # 인접한 칸은 현재 칸과 반대 색이어야 함
        next_color = 'B' if curr_color == 'W' else 'W'
        
        for k in range(4):
            nx, ny = curr_x + dx[k], curr_y + dy[k]
            
            # 8x8 범위를 벗어나지 않는지 확인
            if start_x <= nx < start_x + 8 and start_y <= ny < start_y + 8:
                if not visited[nx - start_x][ny - start_y]:
                    visited[nx - start_x][ny - start_y] = True
                    # 인접한 칸의 실제 색이 예상되는 색(next_color)과 다르면 count 증가
                    if pan[nx][ny] != next_color:
                        count += 1
                    q.append((nx, ny, next_color))
                    
    return count

min_cnt = 64

# 모든 가능한 8x8 시작점에 대해 탐색
for i in range(N - 7):
    for j in range(M - 7):
        # 1. 맨 위 왼쪽이 'W'로 시작하는 경우
        # 2. 맨 위 왼쪽이 'B'로 시작하는 경우
        # 두 가지 중 최솟값을 선택
        res_w = find_paint_bfs(i, j, 'W')
        res_b = find_paint_bfs(i, j, 'B')
        min_cnt = min(min_cnt, res_w, res_b)

print(min_cnt)