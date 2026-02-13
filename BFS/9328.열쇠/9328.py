# 지도의 테두리 확장
#

from collections import deque

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for _ in range(1, T + 1):
    n, m = map(int, input().split())

    info = [list(input().strip()) for _ in range(n)]
    keys = list(input().strip())
    # print(info)
    # print(keys)
    hash_key = [0] * 26
    for key in keys:
        if key == "0":
            break
        idx = ord(key) - ord("a")
        hash_key[idx] = 1

    doors = [[] for _ in range(26)]

    # 어떤 입구든지 (0,0)으로 시작해서 가기 위한 패딩 작업
    graph = [["."] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            graph[i][j] = info[i - 1][j - 1]
    # print(graph)

    visited = [[0] * (m + 2) for _ in range(n + 2)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0))
    cnt = 0
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= (n + 2) or ny >= (m + 2):
                continue
            if graph[nx][ny] == "*":
                continue

            # 문인 경우
            if visited[nx][ny] == 0 and "A" <= graph[nx][ny] <= "Z":
                idx = ord(graph[nx][ny]) - ord("A")
                if hash_key[idx] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                else:
                    doors[idx].append((nx, ny))

            # 열쇠를 찾은 경우
            elif visited[nx][ny] == 0 and "a" <= graph[nx][ny] <= "z":
                idx = ord(graph[nx][ny]) - ord("a")
                visited[nx][ny] = 1
                queue.append((nx, ny))
                # 처음 얻는 열쇠인 경우
                if hash_key[idx] == 0:
                    hash_key[idx] = 1
                    if doors[idx]:
                        for door_x, door_y in doors[idx]:
                            if visited[door_x][door_y] == 0:
                                visited[door_x][door_y] = 1
                                queue.append((door_x, door_y))

            elif visited[nx][ny] == 0 and graph[nx][ny] == "$":
                cnt += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

            elif visited[nx][ny] == 0 and graph[nx][ny] == ".":
                visited[nx][ny] = 1
                queue.append((nx, ny))

    print(cnt)
