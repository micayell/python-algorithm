import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D_time = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)  # 진입 차수
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    target = int(input())

    # 최소 시간 배열 선언
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = D_time[i]

    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        curr = queue.popleft()

        if curr == target:
            break

        for next_building in graph[curr]:
            dp[next_building] = max(dp[next_building], dp[curr] + D_time[next_building])

            in_degree[next_building] -= 1

            if in_degree[next_building] == 0:
                queue.append(next_building)

    print(dp[target])
