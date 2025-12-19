import heapq

n=int(input())
m=int(input())
adj=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,w=map(int,input().split())
    adj[s].append((e,w))

st,ed = map(int,input().split())

arr=[21e8]*(n+1)

def dijkstra(st):
    arr[st]=0
    min_heap=[]
    heapq.heappush(min_heap,(0,st))

    while min_heap:
        cost,current_node=heapq.heappop(min_heap)

        if arr[current_node] < cost:
            continue

        for next_node, next_cost in adj[current_node]:
            new_cost = cost + next_cost
            if new_cost < arr[next_node]:
                arr[next_node] = new_cost
                heapq.heappush(min_heap, (new_cost, next_node))

dijkstra(st)

print(arr[ed])