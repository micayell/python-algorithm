import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


lis_tails = []  # LIS의 길이(정답 배열 X)
pos = [0] * N


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
    if not lis_tails or lis_tails[-1] < nums[i]:
        lis_tails.append(nums[i])
        pos[i] = len(lis_tails) - 1
    else:
        idx = binary_search_left(nums[i])
        lis_tails[idx] = nums[i]
        pos[i] = idx

length = len(lis_tails)
print(length)

result = []
current_target_idx = length - 1

for i in range(N - 1, -1, -1):
    if pos[i] == current_target_idx:
        result.append(nums[i])
        current_target_idx -= 1

print(*(result[::-1]))
