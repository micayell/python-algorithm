import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dist = [21e8] * 100001
dist[N] = 0

pq = []
heapq.heappush(pq, (0, N))
# print(pq)

while pq:
    curr_time, curr_pos = heapq.heappop(pq)

    if curr_time > dist[curr_pos]:
        continue

    if curr_pos == K:
        print(curr_time)
        break

    if curr_pos * 2 <= 100000 and dist[curr_pos * 2] > curr_time:
        dist[curr_pos * 2] = curr_time
        heapq.heappush(pq, (curr_time, curr_pos * 2))

    if curr_pos + 1 <= 100000 and dist[curr_pos + 1] > curr_time + 1:
        dist[curr_pos + 1] = curr_time + 1
        heapq.heappush(pq, (curr_time + 1, curr_pos + 1))

    if curr_pos - 1 >= 0 and dist[curr_pos - 1] > curr_time + 1:
        dist[curr_pos - 1] = curr_time + 1
        heapq.heappush(pq, (curr_time + 1, curr_pos - 1))
