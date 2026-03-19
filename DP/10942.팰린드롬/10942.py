# 팰린드롬 : 앞뒤로 읽어도 똑같은 수열
import sys

input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))

M = int(input())

# 양끝 숫자가 같고, 그 사이에 있는 수열이 팰린드롬이면, 전체도 팰린드롬이다.
# dp[i][j] : i번째부터 j번째까지의 수열이 팰림드롬인지 아닌지
dp = [[0] * (N + 1) for _ in range(N + 1)]

# 길이가 1인 경우
for i in range(1, N + 1):
    dp[i][i] = 1

# 길이가 2인 경우
for i in range(1, N):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1

# 길이가 3이상인 경우
for length in range(3, N + 1):
    for start in range(1, N - length + 2):
        end = start + length - 1

        if nums[start] == nums[end] and dp[start + 1][end - 1] == 1:
            dp[start][end] = 1


for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])
