import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
    exit()
    
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))
# print(tree)

visited = [-1] * (n + 1)


def dfs(node, weight):
    visited[node] = weight

    for next_node, W in tree[node]:
        if visited[next_node] == -1:
            dfs(next_node, weight + W)


dfs(1, 0)
farthest_node = visited.index(max(visited))


visited = [-1] * (n + 1)  # 방문 배열 초기화 => 가장 먼 노드에서부터 시작해야 함
dfs(farthest_node, 0)

print(max(visited))
