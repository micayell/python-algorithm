n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

inf = int(1e9)
graph = [[inf] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    st, ed, cost = map(int, input().split())
    if cost < graph[st][ed]:
        graph[st][ed] = cost
# print(graph)

for a in range(1, n + 1):
    graph[a][a] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == inf:
            graph[i][j] = 0
        print(graph[i][j], end=" ")
    print()
