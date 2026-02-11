N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N
res = []
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

idx = 1
while idx < N:
    for i in range(len(dp)):
        if dp[i] == idx:
            print(arr[i], end=" ")
            break
    idx += 1
