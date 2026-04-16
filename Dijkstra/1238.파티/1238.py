import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())

# X에서 각자 집으로 돌아가는 길
graph = [[] for _ in range(N + 1)]
# 각자 집에서 X로 가는 길
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    reverse_graph[end].append((start, cost))


def dijkstra(start, target_graph):
    distances = [float("inf")] * (N + 1)
    distances[start] = 0
    queue = []

    heapq.heappush(queue, (0, start))

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if distances[current_node] < current_dist:
            continue

        for adjacent_node, weight in target_graph[current_node]:
            cost = current_dist + weight

            if cost < distances[adjacent_node]:
                distances[adjacent_node] = cost
                heapq.heappush(queue, (cost, adjacent_node))

    return distances


home_to_X = dijkstra(X, reverse_graph)
X_to_home = dijkstra(X, graph)

max_time = 0
for i in range(1, N + 1):
    if home_to_X[i] != float("inf") and X_to_home[i] != float("inf"):
        max_time = max(max_time, home_to_X[i] + X_to_home[i])

print(max_time)
