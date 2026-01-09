import heapq


def prim(v, edges):
    mst_value = 0

    graph = [[] for _ in range(v + 1)]
    for s, e, w in edges:
        graph[s].append((w, e))
        graph[e].append((w, s))

    visited = [0] * (v + 1)
    heap = [(0, 1)]

    cnt = 0
    while heap:
        if cnt == v:
            break

        weight, node = heapq.heappop(heap)

        if visited[node] == 0:
            visited[node] = 1
            mst_value += weight
            cnt += 1

            for next_weight, next_node in graph[node]:
                if visited[next_node] == 0:
                    heapq.heappush(heap, (next_weight, next_node))

    return mst_value


v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]

res = prim(v, edges)
print(res)
