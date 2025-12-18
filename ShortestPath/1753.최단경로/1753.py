import heapq

def dijkstra(graph, s):
    distances[s]=0
    min_heap=[]
    heapq.heappush(min_heap, [0,s])

    while min_heap:
        w,u=heapq.heappop(min_heap)

        if distances[u] < w:
            continue

        for u,v,w in graph:
            distance = distances[u] + w
            if distance < distances[v]:
                distances[v]=distance
                heapq.heappush(min_heap,[distance,v])

    return distances


v,e=map(int,input().split())
k=int(input())
graph = [list(map(int,input().split())) for _ in range(e)]
INF=21e8
distances=[INF]*(v+1)

res = dijkstra(graph,k)

for i in range(1,v+1):
    if res[i]==INF:
        print('INF')
    else:
        print(res[i])