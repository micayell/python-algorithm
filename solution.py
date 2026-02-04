import sys

# 빠른 입력을 위해 필수 설정
input = sys.stdin.readline

def solve():
    # 1. 테스트 케이스 개수 T 입력
    t = int(input())
    
    for _ in range(t):
        # 2. 열의 개수 n과 스티커 점수 입력
        n = int(input())
        # stickers[0]은 위쪽 행, stickers[1]은 아래쪽 행
        stickers = [list(map(int, input().split())) for _ in range(2)]
        
        # 3. 예외 처리: n이 1인 경우 바로 출력하고 다음 케이스로
        if n == 1:
            print(max(stickers[0][0], stickers[1][0]))
            continue
        
        # 4. DP 테이블 선언 및 초기화
        dp = [[0] * n for _ in range(2)]
        
        # 첫 번째 열 초기화
        dp[0][0] = stickers[0][0]
        dp[1][0] = stickers[1][0]
        
        # 두 번째 열 초기화 (무조건 대각선에서 와야 함)
        dp[0][1] = stickers[1][0] + stickers[0][1]
        dp[1][1] = stickers[0][0] + stickers[1][1]
        
        # 5. 세 번째 열(인덱스 2)부터 점화식 진행
        for i in range(2, n):
            # i번째 위쪽 스티커를 떼는 경우:
            # i-1번째 아래쪽 혹은 i-2번째 아래쪽 중 큰 값을 선택
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
            
            # i번째 아래쪽 스티커를 떼는 경우:
            # i-1번째 위쪽 혹은 i-2번째 위쪽 중 큰 값을 선택
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]
            
        # 6. 마지막 열의 두 값 중 최댓값 출력
        print(max(dp[0][n-1], dp[1][n-1]))

if __name__ == "__main__":
    solve()