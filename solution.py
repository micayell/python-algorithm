bridge = [0] * w  # 다리 길이만큼 0으로 초기화
time = 0
current_weight = 0

while bridge:  # 다리에 칸이 남아있는 동안
    time += 1
    current_weight -= bridge.pop(0)  # 다리 맨 앞 칸을 비움

    if 대기_트럭_리스트:
        if current_weight + 대기_트럭_리스트[0] <= L:
            truck = 대기_트럭_리스트.pop(0)
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)  # 못 올라오면 빈 공간 추가
from collections import deque

# 다리 길이 w, 최대 하중 l
bridge = deque([0] * w) 
trucks = deque(truck_weights) # 대기 중인 트럭들도 deque로 관리하면 편함

time = 0
current_weight = 0 # 현재 다리 위의 총 무게

while bridge:
    time += 1
    # 1. 다리에서 트럭(또는 빈 공간)이 나감
    out = bridge.popleft()
    current_weight -= out
    
    # 2. 대기 중인 트럭이 있는지 확인
    if trucks:
        # 새 트럭이 올라올 수 있으면
        if current_weight + trucks[0] <= l:
            t = trucks.popleft()
            bridge.append(t)
            current_weight += t
        # 무게 초과로 못 올라오면 빈 공간(0)을 채움
        else:
            bridge.append(0)

    # 3. 만약 대기 트럭도 없고 다리도 비었으면 종료인데, 
    # 위 로직대로면 마지막 트럭이 다리에 올라가는 순간까지만 계산될 수 있음
    # (세부 종료 조건은 구현 방식에 따라 살짝 다를 수 있습니다)