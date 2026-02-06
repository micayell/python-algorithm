import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
    exit()  # 프로그램을 끝내는 명령어

tree = {}
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    if p not in tree:
        tree[p] = {}
    if c not in tree:
        tree[c] = {}
    tree[p][c] = w
    tree[c][p] = w
# print(tree)

visited = [-1] * (n + 1)


def dfs(node, weight):
    if node not in tree:
        return

    visited[node] = weight

    for next_node, plus_weight in tree[node].items():
        if visited[next_node]==-1:
            dfs(next_node, weight + plus_weight)


dfs(1, 0)
farthest_node = visited.index(max(visited))

visited = [-1] * (n + 1)
dfs(farthest_node, 0)

print(max(visited))
