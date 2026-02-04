import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

parents = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def find_parent(curr):
    for next_node in graph[curr]:
        if parents[next_node] == 0:
            parents[next_node] = curr
            find_parent(next_node)


parents[1] = -1
find_parent(1)
for i in range(2, N + 1):
    print(parents[i])
