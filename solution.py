import copy

# 1. 방향 정의 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 2. CCTV별 감시 방향 설정
# 예: 3번 CCTV는 [0, 1], [1, 2], [2, 3], [3, 0] 방향 세트 가능
mode = [
    [],
    [[0], [1], [2], [3]],           # 1번
    [[0, 2], [1, 3]],               # 2번
    [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번
    [[0, 1, 2, 3]]                  # 5번
]

def fill(board, mm, x, y):
    """특정 방향세트(mm)로 감시 영역(#)을 채우는 함수"""
    for i in mm:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            # 범위를 벗어나거나 벽(6)을 만나면 중단
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 6:
                break
            # 빈칸(0)인 경우만 감시 영역(#)으로 표시
            if board[nx][ny] == 0:
                board[nx][ny] = '#'

def dfs(depth, arr):
    global min_value
    # 모든 CCTV를 확인했을 때 사각지대 계산
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return

    # 현재 단계의 CCTV 정보 꺼내기
    x, y, cctv_type = cctv[depth]
    
    # 해당 CCTV가 가질 수 있는 모든 방향 조합 시도
    for mm in mode[cctv_type]:
        # 현재 지도 상태 복사 (Deep Copy)
        temp = copy.deepcopy(arr)
        # 감시 영역 채우기
        fill(temp, mm, x, y)
        # 다음 CCTV로 이동
        dfs(depth + 1, temp)

# 입력 처리
n, m = map(int, input().split())
graph = []
cctv = []

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        # CCTV 위치와 종류 저장 (1~5번)
        if 1 <= data[j] <= 5:
            cctv.append((i, j, data[j]))

min_value = float('inf')
dfs(0, graph)
print(min_value)