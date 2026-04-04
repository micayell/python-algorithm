N = int(input())

matrix = []
for _ in range(N):
    r, c = map(int, input().split())
    matrix.append((r, c))

dp = [[float("inf")] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0

for L in range(2, N + 1):
    for st in range(N - L + 1):
        ed = st + L - 1

        for k in range(st, ed):
            cross_mode = matrix[st][0] * matrix[k][1] * matrix[ed][1]
            total_mode = dp[st][k] + dp[k + 1][ed] + cross_mode

            if total_mode < dp[st][ed]:
                dp[st][ed] = total_mode

print(dp[0][N - 1])
