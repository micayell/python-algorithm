# LCS(최소공통조상), Sparse_Table(희소배열), DFS
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())

LOG = 16
tree = [[] for _ in range(N + 1)]
depth = [0] * (N + 1)
dist = [0] * (N + 1)
parent = [[0] * LOG for _ in range(N + 1)]


# 1. 루트 노드부터 탐색하여 깊이, 거리, 1차 부모를 기록하는 함수
def DFS(cur, p, d, dep):  # 현재노드, 부모노드, 누적거리, 현재깊이
    depth[cur] = dep
    dist[cur] = d
    parent[cur][0] = p

    for nxt, cost in tree[cur]:
        if nxt != p:
            DFS(nxt, cur, d + cost, dep + 1)


# 2. DP를 이용해 조상 배열(희소 배열)을 갱신하는 함수
def set_parent():
    DFS(1, 0, 0, 0)

    # parent[i][j] = i번 노드의 2^j번째 조상
    for j in range(1, LOG):
        for i in range(1, N + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]


# 3. 두 노드의 최소 공통 조상을 찾는 함수
def get_LCA(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    # 1단계: a와 b의 깊이 맞추기
    for i in range(LOG - 1, -1, -1):
        if depth[a] - depth[b] >= (1 << i):
            a = parent[a][i]

    # 깊이를 맞췄는데 두 노드가 같다면, 그것이 곧 LCA
    if a == b:
        return a

    # 2단계: 공통 조상 바로 아래까지 노드 끌어올리기
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    # a와 b의 바로 윗 부모가 LCS임
    return parent[a][0]


for _ in range(N - 1):
    u, v, cost = map(int, input().split())
    tree[u].append((v, cost))
    tree[v].append((u, cost))

set_parent()

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    lca_node = get_LCA(a, b)
    ans = dist[a] + dist[b] - (2 * dist[lca_node])
    print(ans)
