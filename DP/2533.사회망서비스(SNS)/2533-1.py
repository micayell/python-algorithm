# pypy로는 메모리 초과, python3으로 통과했지만 pypy 제출용

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# dp[node][0] : 현재 노드가 얼리아답터가 아닐때, 해당 서브트리에서 필요한 최소 얼리아답터 수
# dp[node][1] : 현재 노드가 얼리아답터일 때, 해당 서브트리에서 필요한 최소 얼리아답터 수
dp = [[0, 1] for _ in range(N + 1)]


def dfs(curr, prev):

    for nxt in tree[curr]:
        if nxt != prev:  # 연결된 노드가 부모 노드가 아니라면 무조건 자식 노드임
            dfs(nxt, curr)
            # ex) 1번이 얼리(X)일 때: 3번은 무조건 얼리(O)여야 함
            dp[curr][0] += dp[nxt][1]
            dp[curr][1] += min(dp[nxt][0], dp[nxt][1])


dfs(1, -1)
print(min(dp[1][0], dp[1][1]))
