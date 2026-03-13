import sys

# 입력 처리
C, N = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dp[i]는 i명의 고객을 모으기 위한 최소 비용
# 인원수는 C보다 커질 수 있으므로 (최대 추가 인원 100), C + 100까지 여유있게 설정
dp = [float('inf')] * (C + 101)
dp[0] = 0

for cost, people in info:
    for i in range(people, C + 101):
        # 현재 i명을 모으는 비용 vs (i - people)명을 모으는 비용 + 현재 도시 홍보 비용
        dp[i] = min(dp[i], dp[i - people] + cost)

# '적어도 C명'이므로 C부터 마지막 인덱스까지 중 최솟값 출력
print(min(dp[C:]))