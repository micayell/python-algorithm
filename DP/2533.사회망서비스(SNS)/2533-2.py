# pypy로는 메모리 초과, python3으로 통과했지만 pypy 제출용

import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 1] for _ in range(N + 1)]

# 각 노드의 부모가 누구인지 기억할 배열
parent = [0] * (N + 1)
visited = [False] * (N + 1)

# 1. 탐색 순서를 기록할 리스트
order = []
stack = [1]
visited[1] = True

# DFS를 재귀 대신 while문으로 구현 (Top-down 탐색)
while stack:
    curr = stack.pop()
    order.append(curr)  # 방문한 순서대로 기록 (부모 -> 자식 순서가 됨)

    for nxt in tree[curr]:
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = curr  # 다음 노드의 부모를 현재 노드로 기록
            stack.append(nxt)

# 2. order 리스트를 뒤에서부터 거꾸로 순회 (Bottom-up 계산)
# 맨 뒤에 있는 노드(단말 노드)부터 루트 노드 방향으로 올라옵니다.
for i in range(len(order) - 1, -1, -1):
    curr = order[i]
    p = parent[curr]

    # 루트 노드(부모가 0)가 아니라면, 내 결과를 부모의 DP에 더해줌
    if p != 0:
        dp[p][0] += dp[curr][1]
        dp[p][1] += min(dp[curr][0], dp[curr][1])

print(min(dp[1][0], dp[1][1]))
