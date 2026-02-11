import sys
from copy import deepcopy

# 입력 받기
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def rotate_90(board):
    """보드를 시계 방향으로 90도 회전시키는 함수"""
    new_board = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_board[c][n - 1 - r] = board[r][c]
    return new_board

def move_left(board):
    """모든 블록을 왼쪽으로 미는 함수 (합치기 로직 포함)"""
    new_board = [[0] * n for _ in range(n)]
    
    for i in range(n):
        # 1. 0을 제외한 숫자들만 모으기
        nums = [x for x in board[i] if x != 0]
        
        # 2. 왼쪽부터 인접한 같은 숫자 합치기
        merged = []
        skip = False
        for j in range(len(nums)):
            if skip:
                skip = False
                continue
            
            if j + 1 < len(nums) and nums[j] == nums[j+1]:
                merged.append(nums[j] * 2)
                skip = True  # 합쳐진 뒷 숫자는 건너뜀
            else:
                merged.append(nums[j])
        
        # 3. 새로운 보드에 채워 넣기 (나머지는 0)
        for j in range(len(merged)):
            new_board[i][j] = merged[j]
            
    return new_board

def dfs(board, depth):
    """5번 이동하는 모든 경우의 수를 탐색 (DFS)"""
    global answer
    
    # 기저 사례: 5번 이동 시 최대 블록 값 갱신
    if depth == 5:
        for row in board:
            answer = max(answer, max(row))
        return

    # 4방향 시뮬레이션
    temp_board = deepcopy(board)
    for _ in range(4):
        # 왼쪽으로 밀기 수행
        moved_board = move_left(temp_board)
        # 다음 단계 탐색
        dfs(moved_board, depth + 1)
        # 보드를 90도 회전시켜 다음 루프에서 다른 방향을 왼쪽으로 밀 수 있게 함
        temp_board = rotate_90(temp_board)

# 초기화 및 실행
answer = 0
dfs(board, 0)
print(answer)