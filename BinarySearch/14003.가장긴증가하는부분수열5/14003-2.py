import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# LIS를 유지하기 위한 배열 (실제 LIS 수열은 아님)
lis_tails = []
# 각 원소가 lis_tails의 어느 인덱스에 들어갔는지 기록 (역추적용)
pos = [0] * N

# bisect_left 기능을 하는 이분 탐색 함수 직접 구현
def binary_search_left(target):
    low = 0
    high = len(lis_tails)
    
    while low < high:
        mid = (low + high) // 2
        if lis_tails[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

for i in range(N):
    if not lis_tails or lis_tails[-1] < arr[i]:
        # 현재 원소가 LIS의 마지막 값보다 크면 뒤에 추가
        lis_tails.append(arr[i])
        pos[i] = len(lis_tails) - 1
    else:
        # 이분 탐색으로 들어갈 위치를 찾아 값 교체 (O(log N))
        idx = binary_search_left(arr[i])
        lis_tails[idx] = arr[i]
        pos[i] = idx

# 1. LIS의 길이 출력
length = len(lis_tails)
print(length)

# 2. 역추적 (Backtracking)으로 실제 수열 찾기
# pos 배열에는 각 원소가 LIS 빌드업 과정에서 가졌던 '순서'가 저장되어 있음
result = []
current_target_idx = length - 1

for i in range(N - 1, -1, -1):
    if pos[i] == current_target_idx:
        result.append(arr[i])
        current_target_idx -= 1

# 뒤에서부터 담았으므로 뒤집어서 출력
print(*(result[::-1]))