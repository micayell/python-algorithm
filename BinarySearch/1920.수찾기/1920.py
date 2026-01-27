N = int(input())
N_arr = list(map(int, input().split()))
N_arr.sort()

M = int(input())
M_arr = list(map(int, input().split()))

for m in M_arr:
    if m in N_arr:
        print(1)
    else:
        print(0)