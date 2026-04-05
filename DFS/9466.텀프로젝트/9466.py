import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(curr):
    global result

    visited[curr] = 1
    next_node = graph[curr]
    cycle_path.append(curr)

    if visited[next_node]:
        if next_node in cycle_path:
            result += len(cycle_path[cycle_path.index(next_node) :])
        return
    else:
        dfs(next_node)


T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))

    visited = [0] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            cycle_path = []
            dfs(i)

    # 전체인원수 - cycle된 인원 수
    print(n - result)
