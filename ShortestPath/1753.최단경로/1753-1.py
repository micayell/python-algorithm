import heapq

def dijkstra(s):
    distances[s]=0
    min_heap=[]
    heapq.heappush(min_heap, [0,s])

    while min_heap:
        dist,u=heapq.heappop(min_heap)

        if distances[u] < dist:
            continue

        for v,w in adj[u]:
            cost = dist + w
            if cost < distances[v]:
                distances[v]=cost
                heapq.heappush(min_heap,[cost,v])



v,e=map(int,input().split())
k=int(input())

adj=[[] for _ in range(v+1)]
for _ in range(e):
    u,node_v,w=map(int,input().split())
    adj[u].append((node_v,w))

INF=21e8
distances=[INF]*(v+1)

dijkstra(k)

for i in range(1,v+1):
    if distances[i]==INF:
        print('INF')
    else:
        print(distances[i])