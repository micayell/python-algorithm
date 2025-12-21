import heapq

n,e = map(int,input().split())

adj=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

v1,v2=map(int,input().split())


st=1
ed=n

def dijkstra(st):
    distances=[1e9]*(n+1)
    distances[st]=0
    min_heap=[]
    heapq.heappush(min_heap,(0,st))

    while min_heap:
        cur_dist, cur_node=heapq.heappop(min_heap)

        if distances[cur_node] < cur_dist:
            continue

        for next_node, next_dist in adj[cur_node]:
            new_dist = cur_dist + next_dist
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(min_heap, (new_dist, next_node))
    return distances

dist_st = dijkstra(st)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist_st[v1] + dist_v1[v2] + dist_v2[n]
path2 = dist_st[v2] + dist_v2[v1] + dist_v1[n]

res = min(path1, path2)

if res >= 1e9:
    print("-1")
else:
    print(res)