import heapq
from collections import deque # 대기열을 위해 큐 사용

TC = int(input())

for t in range(1, TC + 1):
    n, m = map(int, input().split())
    
    # R_arr: 단위 무게당 요금 (인덱스 맞추기 위해 0번지에는 0을 넣거나, 쓸때 -1 처리)
    R_arr = [int(input()) for _ in range(n)]
    
    # W_arr: 차량의 무게
    W_arr = [int(input()) for _ in range(m)]
    
    # X_arr: 차량 출입 순서 (2*m개)
    # 한 번에 다 입력받아 리스트로 만드는 게 편합니다.
    X_arr = [int(input()) for _ in range(2 * m)]

    # 1. [핵심] 빈 주차 공간을 관리하는 '최소 힙'
    # 0번 주차장 ~ n-1번 주차장이 비어있으므로 힙에 다 넣어둡니다.
    empty_spots = []
    for i in range(n):
        heapq.heappush(empty_spots, i)
    
    # 2. 대기하는 차들을 위한 '큐'
    waiting_queue = deque()

    # 3. 어떤 차가 어디 주차했는지 기억장소 (차량번호 -> 주차자리)
    # 차량번호는 1~m까지 있으므로 m+1 크기로 만듦
    car_location = [0] * (m + 1)

    result = 0

    # 순서대로 하나씩 처리
    for car in X_arr:
        if car > 0: # 1. 차량 들어옴 (입차)
            # 빈 자리가 있다면?
            if empty_spots:
                # 가장 번호가 작은 자리를 꺼낸다 (힙의 장점!)
                spot_idx = heapq.heappop(empty_spots)
                
                # 요금 계산: 무게 * 단위요금
                result += W_arr[car-1] * R_arr[spot_idx]
                
                # 위치 기록: car번 차는 spot_idx에 주차함
                car_location[car] = spot_idx
            else:
                # 자리가 없으면 대기열에 넣음
                waiting_queue.append(car)

        else: # 2. 차량 나감 (출차)
            out_car = -car # 음수니까 양수로 바꿔줌 (예: -3 -> 3번 차 나감)
            
            # 이 차가 썼던 자리를 알아냄
            free_spot = car_location[out_car]

            # [중요] 자리가 났는데, 기다리는 차가 있다면?
            if waiting_queue:
                # 기다리던 차를 바로 그 자리에 넣음 (빈 자리를 힙에 넣을 새도 없이)
                next_car = waiting_queue.popleft()
                
                result += W_arr[next_car-1] * R_arr[free_spot]
                car_location[next_car] = free_spot
            
            else:
                # 기다리는 차가 없으면, 이 자리는 다시 빈 자리 힙으로 반납
                heapq.heappush(empty_spots, free_spot)

    print(f'#{t} {result}')