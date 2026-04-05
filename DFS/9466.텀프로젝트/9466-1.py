# dfs함수 사용하지 않고 while문 사용해서 풀기

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))

    visited = [0] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            cycle_path = []
            curr = i  # 현재 노드를 i로 시작

            while 1:
                visited[curr] = 1
                cycle_path.append(curr)
                next_node = graph[curr]

                # 다음 노드를 이미 방문했다면?
                if visited[next_node]:
                    if next_node in cycle_path:
                        result += len(cycle_path[cycle_path.index(next_node) :])
                    break

                else:
                    curr = next_node

    # 전체인원수 - cycle된 인원 수
    print(n - result)
