from collections import deque


def get_road_move_time():
    queue = deque([(0, 0)])
    distance = [[-1] * M for _ in range(N)]
    distance[0][0] = 0

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            next_x = x + dx
            next_y = y + dy
            if (
                0 <= next_x < N
                and 0 <= next_y < M
                and data[next_x][next_y]
                and distance[next_x][next_y] == -1
            ):
                queue.append((next_x, next_y))
                distance[next_x][next_y] = distance[x][y] + 1
                if next_x == N - 1 and next_y == M - 1:
                    return distance[next_x][next_y]
    return -1


N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
# print(data)
result = get_road_move_time() + 1
print(result)
