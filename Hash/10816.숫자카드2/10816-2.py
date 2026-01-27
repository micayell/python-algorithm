import sys

# 입출력 최적화
input = sys.stdin.readline

def get_lower_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

def get_upper_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start

# 1. 입력 및 정렬
n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

# 2. 각 쿼리에 대해 이분 탐색 수행
results = []
for target in m_list:
    lb = get_lower_bound(n_list, target)
    ub = get_upper_bound(n_list, target)
    results.append(ub - lb)

# 3. 결과 한 번에 출력
print(*(results))