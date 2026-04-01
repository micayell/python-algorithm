import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

queue = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

answer = []
while queue:
    curr = queue.popleft()
    answer.append(curr)

    for nxt in graph[curr]:
        in_degree[nxt] -= 1

        if in_degree[nxt] == 0:
            queue.append(nxt)

print(*answer)
