N = int(input())

dp = [0] * (N + 1)
parent = [0] * (N + 1)
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    parent[i] = i - 1
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        parent[i] = i // 2
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        parent[i] = i // 3

print(dp[N])

curr = N
while 1:
    if curr == 1:
        print(curr)
        break
    print(curr, end=" ")
    curr = parent[curr]
