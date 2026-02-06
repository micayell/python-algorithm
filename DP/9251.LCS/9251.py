S1 = input()
S2 = input()

if len(S1) < len(S2):
    S1, S2 = S2, S1
n = len(S1)
m = len(S2)

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if S1[i - 1] == S2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        if S1[i - 1] != S2[j - 1]:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[n][m])
