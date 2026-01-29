N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [0] * (N + 1)


def dfs(point):
    visited[point] = 1
    for p in arr[point]:
        if not visited[p]:
            dfs(p)


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
