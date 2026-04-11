# 파이썬은 1초에 보통 2000만번 이상의 연산

import sys
import heapq

input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    h, o = map(int, input().split())
    lines.append((min(h, o), max(h, o)))

d = int(input())

valid_lines = []
for h, o in lines:
    start = min(h, o)
    end = max(h, o)

    if (end - start) <= d:
        valid_lines.append((start, end))

valid_lines.sort(key=lambda x: (x[1], x[0]))

min_heap = []
max_cnt = 0
for start, end in valid_lines:
    heapq.heappush(min_heap, start)

    rail_start = end - d
    while min_heap and min_heap[0] < rail_start:
        heapq.heappop(min_heap)

    max_cnt = max(max_cnt, len(min_heap))

print(max_cnt)
