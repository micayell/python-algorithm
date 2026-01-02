import heapq

T=int(input())
for t in range(1,T+1):
    min_heap=[]
    max_heap=[]
    
    k=int(input())
    visited=[0]*k

    for i in range(k):
        s,n=input().split()
        num=int(n)

        if s=='I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num,i))
            visited[i]=1

        elif s=='D':
            if n=='1' and max_heap:
                while not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                val,idx=heapq.heappop(max_heap)
                visited[idx]=0

            if n=='-1' and min_heap:
                while not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                val,idx=heapq.heappop(min_heap)
                visited[idx]=0

        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)

        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)

    if not max_heap or not min_heap:
        print('EMPTY')

    else:
        max_val=-heapq.heappop(max_heap)[0]
        min_val=heapq.heappop(min_heap)[0]
        print(max_val, min_val)