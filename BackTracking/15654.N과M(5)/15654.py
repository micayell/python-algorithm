N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * N


def dfs(res):
    if len(res) == M:
        print(*res)
        return

    for i in range(len(nums)):
        if visited[i] == 0:
            visited[i] = 1
            res.append(nums[i])
            dfs(res)
            res.pop()
            visited[i] = 0


dfs([])
