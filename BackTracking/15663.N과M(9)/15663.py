import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0] * (N)


def dfs(res):
    if len(res) == M:
        print(*res)
        return

    last_used = 0
    for i in range(N):
        if visited[i] == 0 and last_used != nums[i]:
            last_used = nums[i]
            visited[i] = 1
            res.append(nums[i])
            dfs(res)
            res.pop()
            visited[i] = 0


dfs([])
