import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

lis_tails = []


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
    else:
        idx = binary_search_left(nums[i])
        lis_tails[idx] = nums[i]

print(len(lis_tails))
