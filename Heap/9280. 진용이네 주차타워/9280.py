import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(current_dir,'input.txt'),'r')

import heapq
from collections import deque

TC=int(input())

for t in range(1, TC+1):
    n,m=map(int,input().split())
    # 단위 무게당 요금
    R_arr = [int(input()) for _ in range(n)]
    # 차량의 무게
    W_arr = [int(input()) for _ in range(m)]
    # 차량의 출입 순서
    X_arr = [int(input()) for _ in range(2*m)]

    empty_spots=[]
    for i in range(n):
        heapq.heappush(empty_spots, i)
    
    waiting_queue = deque()
    # 자동차 인덱스에 n개의 주차공간 중 현재 어느 위치에 있는지 저장
    car_location=[0]*(m+1)
    result = 0

    for car in X_arr:
        if car > 0:
            if empty_spots:
                idx = heapq.heappop(empty_spots)
                result += W_arr[car-1]*R_arr[idx]
                car_location[car] = idx
            else:
                waiting_queue.append(car)

        else:
            out_car = -car
            free_spot = car_location[out_car]

            if waiting_queue:
                next_car = waiting_queue.popleft()
                result += W_arr[next_car-1]*R_arr[free_spot]
                car_location[next_car] = free_spot

            else:
                heapq.heappush(empty_spots, free_spot) # 힙 리스트에 차량 인덱스 추가
            

    print(f'#{t} {result}')