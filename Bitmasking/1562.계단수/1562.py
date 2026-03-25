MOD = 1000000000
N = int(input())  # 계단수의 길이

dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]

# 초기값 세팅 (length가 1일 때)
for i in range(1, 10):
    init_mask = 1 << i
    dp[1][i][init_mask] = 1

# dp[현재_길이][마지막_숫자][현재_마스크]
for length in range(1, N):
    for last in range(10):
        for mask in range(1024):
            curr = dp[length][last][mask]

            if curr == 0:
                continue

            # 다음 숫자가 한 칸 낮아지는 경우
            if last > 0:
                next_num = last - 1
                next_mask = mask | (1 << next_num)
                dp[length + 1][next_num][next_mask] = (
                    dp[length + 1][next_num][next_mask] + curr
                ) % MOD

            # 다음 숫자가 한 칸 높아지는 경우
            if last < 9:
                next_num = last + 1
                next_mask = mask | (1 << next_num)
                dp[length + 1][next_num][next_mask] = (
                    dp[length + 1][next_num][next_mask] + curr
                ) % MOD

answer = 0
for i in range(10):
    answer = (answer + dp[N][i][1023]) % MOD

print(answer)
