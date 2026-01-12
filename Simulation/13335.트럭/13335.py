# 다리를 건너는 트럭의 수, 다리의 길이, 다리의 최대하중
n, w, L = map(int, input().split())

# i번째 트럭의 무게
truck_weights = list(map(int, input().split()))

bridge = [0] * w  # 다리 길이만큼 0으로 초기화
time = 0
current_weight = 0

while bridge:  # 다리에 칸이 남아있는 동안
    time += 1
    current_weight -= bridge.pop(0)  # 다리 맨 앞 칸을 비움

    if truck_weights:
        if current_weight + truck_weights[0] <= L:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)  # 못 올라오면 빈 공간 추가


print(time)
