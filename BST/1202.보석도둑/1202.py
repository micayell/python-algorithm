# 보석 개수, 가방 개수
# 각 보석의 무게, 가격
# 각 가방에 담을 수 있는 무게

import heapq

n,k = map(int,input().split())

bosuk=[]
for _ in range(n):
    heapq.heappush(bosuk,tuple(map(int,input().split())))


bags=[int(input()) for _ in range(k)]
bags.sort()

res=0
temp=[]
for bag in bags:
    while bosuk and bag >= bosuk[0][0]:
        heapq.heappush(temp,-heapq.heappop(bosuk)[1])
    
    if temp:
        res -= heapq.heappop(temp)
    elif not bosuk:
        break
    
print(res)
