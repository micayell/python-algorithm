from collections import deque

import sys
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N + 1)]

parents = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    queue = deque([1])
    parents[1] = -1
    while queue:
        curr = queue.popleft()
        for next_node in graph[curr]:
            if parents[next_node] == 0:
                parents[next_node] = curr
                queue.append(next_node)


bfs()

for i in range(2, N + 1):
    print(parents[i])
