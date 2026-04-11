import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # W명으로 구성된 특수부대를 여러 구역에 '출동'시켜 모든 구역을 방어하는 최소 소대 수 구하기
    N, W = map(int, input().split())  # 구역의 개수/2, 특수 소대원 수
    enemy = [list(map(int, input().split())) for _ in range(2)]

    u = [0] + enemy[0]  # 위쪽 (안쪽 원, 사진의 1~8번)
    d = [0] + enemy[1]  # 아래쪽 (바깥쪽 원, 사진의 9~16번)

    # N=1인 경우: 가로로 묶을 수 없으므로 세로로 묶이는지만 확인 후 빠른 종료
    if N == 1:
        if u[1] + d[1] <= W:
            print(1)
        else:
            print(2)
        continue

    answer = float("inf")

    # DP 점화식 계산 함수
    def run_dp(a, b, c, u_arr, d_arr):
        for i in range(2, N + 1):
            # b[i]: 위쪽만 채워진 상태
            b[i] = a[i - 1] + 1
            if u_arr[i] + u_arr[i - 1] <= W:
                b[i] = min(b[i], c[i - 1] + 1)

            # c[i]: 아래쪽만 채워진 상태
            c[i] = a[i - 1] + 1
            if d_arr[i] + d_arr[i - 1] <= W:
                c[i] = min(c[i], b[i - 1] + 1)

            # a[i]: 위쪽과 아래쪽 모두 채워진 상태 => 경우가 3가지가 있음
            # 경우 1: 따로따로 한칸씩 채우기
            a[i] = min(b[i] + 1, c[i] + 1)
            # 경우 2: 위아래 세로로 묶기
            if u_arr[i] + d_arr[i] <= W:
                a[i] = min(a[i], a[i - 1] + 1)
            # 경우 3: 위쪽 가로 묶고 아래쪽도 가로로 묶기
            if u_arr[i] + u_arr[i - 1] <= W and d_arr[i] + d_arr[i - 1] <= W:
                a[i] = min(a[i], a[i - 2] + 2)

    # Case 0 : 양 끝(1번과 N번)을 전혀 묶지 않은 평범한 1차원 상태
    # (사진 기준: 1번과 8번 안 묶음, 9번과 16번도 안 묶음)
    a, b, c = (
        [float("inf")] * (N + 1),
        [float("inf")] * (N + 1),
        [float("inf")] * (N + 1),
    )
    a[0] = 0
    a[1] = 1 if u[1] + d[1] <= W else 2
    b[1] = 1
    c[1] = 1

    run_dp(a, b, c, u, d)
    answer = min(answer, a[N])

    # Case 1 : 위쪽(안쪽 원)의 양 끝만 특수 소대 1개로 묶은 상태
    # (사진 기준: 1번과 8번을 미리 묶어버림)
    if u[1] + u[N] <= W:
        a, b, c = (
            [float("inf")] * (N + 1),
            [float("inf")] * (N + 1),
            [float("inf")] * (N + 1),
        )
        a[0] = 0
        a[1] = 1
        b[1] = (
            0  # 위쪽 1번은 이미 8번과 묶여서 방어되었으므로, 1번 칸을 채우는 추가 소대 비용은 0이다
        )
        c[1] = float("inf")

        u_temp = u[:]
        u_temp[1] = float("inf")  # 위쪽 1번이 2번과 중복으로 묶이는 것 방지

        run_dp(a, b, c, u_temp, d)
        answer = min(answer, c[N] + 1)

    # Case 2 : 아래쪽(바깥쪽 원)의 양 끝만 특수 소대 1개로 묶은 상태
    # (사진 기준: 9번과 16번을 미리 묶어버림)
    if d[1] + d[N] <= W:
        a, b, c = (
            [float("inf")] * (N + 1),
            [float("inf")] * (N + 1),
            [float("inf")] * (N + 1),
        )
        a[0] = 0
        a[1] = 1
        b[1] = float("inf")
        c[1] = 0  # 아래쪽 1번(9)은 N번과 결합하여 이미 방어되었으므로 비용 0

        d_temp = d[:]
        d_temp[1] = float("inf")  # 아래쪽 1번이 2번과 중복으로 묶이는 것 방지

        run_dp(a, b, c, u, d_temp)
        answer = min(
            answer, b[N] + 1
        )  # 마지막 N번째는 위쪽만 채우면 됨 (미리 쓴 소대 1개 더해줌)

    # Case 3 : 위쪽과 아래쪽 모두 각각 양 끝을 묶은 상태
    # (사진 기준: 1-8 묶고, 9-16도 묶음)
    if u[1] + u[N] <= W and d[1] + d[N] <= W:
        a, b, c = (
            [float("inf")] * (N + 1),
            [float("inf")] * (N + 1),
            [float("inf")] * (N + 1),
        )
        a[0] = 0
        a[1] = 0
        b[1] = float("inf")
        c[1] = float("inf")

        u_temp = u[:]
        d_temp = d[:]
        u_temp[1] = float("inf")
        d_temp[1] = float("inf")

        run_dp(a, b, c, u_temp, d_temp)
        answer = min(answer, a[N - 1] + 2)

    print(answer)
