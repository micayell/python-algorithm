N = int(input())
N_arr = list(map(int, input().split()))
N_arr.sort()

M = int(input())
M_arr = list(map(int, input().split()))

for target in M_arr:
    low, high = 0, N - 1
    flag = 0
    while low <= high:
        mid = (low + high) // 2
        if N_arr[mid] == target:
            flag = 1
            break
        elif N_arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    if flag:
        print(1)
    else:
        print(0)
