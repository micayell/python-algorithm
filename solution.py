import sys

# 1. 재귀 깊이 제한 해제 (중요!)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit()

# 2. 인접 리스트 생성 (양방향 연결)
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w)) # 부모<->자식 양방향으로 연결해야 어디든 이동 가능

def dfs(node, current_dist, visited):
    visited[node] = current_dist
    
    for next_node, weight in adj[node]:
        if visited[next_node] == -1: # 방문하지 않은 노드라면
            dfs(next_node, current_dist + weight, visited)

# --- 실행 부분 ---

# [1단계] 1번 노드에서 가장 먼 노드 찾기
visited1 = [-1] * (n + 1)
dfs(1, 0, visited1)

# 1번에서 가장 먼 노드 번호 찾기
farthest_node = visited1.index(max(visited1))

# [2단계] 그 노드(farthest_node)에서 가장 먼 노드까지의 거리 구하기
visited2 = [-1] * (n + 1)
dfs(farthest_node, 0, visited2)

# 결과 출력
print(max(visited2))