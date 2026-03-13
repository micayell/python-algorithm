import sys

def solve():
    # 입력 받기
    n = int(sys.stdin.readline())
    solution = list(map(int, sys.stdin.readline().split()))

    ans_abs_sum = float('inf')
    ans_pair = [0, 0]

    # 1. 첫 번째 용액을 하나씩 고정 (마지막 용액 전까지)
    for i in range(n - 1):
        current = solution[i]
        
        # 2. i번째 이후 범위에서 -current와 가장 가까운 값을 찾기 위한 이진 탐색
        st = i + 1
        ed = n - 1
        
        while st <= ed:
            mid = (st + ed) // 2
            temp_sum = current + solution[mid]
            
            # 절대값이 현재까지의 최소값보다 작으면 갱신
            if abs(temp_sum) < ans_abs_sum:
                ans_abs_sum = abs(temp_sum)
                ans_pair = [current, solution[mid]]
            
            if temp_sum == 0:
                print(f"{ans_pair[0]} {ans_pair[1]}")
                return # 0을 찾으면 즉시 종료
            
            # 합이 0보다 작으면 더 큰 값을 찾아야 함
            if temp_sum < 0:
                st = mid + 1
            # 합이 0보다 크면 더 작은 값을 찾아야 함
            else:
                ed = mid - 1

    print(f"{ans_pair[0]} {ans_pair[1]}")

solve()