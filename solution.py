import sys

# 백준 시간 초과 방지를 위해 input()을 sys.stdin.readline으로 덮어씌움
input = sys.stdin.readline


def solve():
    T = int(input())

    for _ in range(T):
        N, W = map(int, input().split())
        enemy = [list(map(int, input().split())) for _ in range(2)]

        # 기존 DP 로직과 맞추기 위해 (1-based indexing) 맨 앞에 더미 값(0)을 추가
        u = [0] + enemy[0]
        d = [0] + enemy[1]

        # N=1 인 경우 (원형 구조를 고려할 필요 없이 바로 세로로 묶을 수 있는지만 판단)
        if N == 1:
            if u[1] + d[1] <= W:
                print(1)
            else:
                print(2)
            continue

        ans = float("inf")

        # 가독성을 높인 DP 수행 내부 함수
        def run_dp(a, b, c, u_arr, d_arr):
            for i in range(2, N + 1):
                # --- b[i] 계산 (i번째 열 위쪽만 채워진 상태) ---
                # 1. 단독 배치 (항상 가능)
                b[i] = a[i - 1] + 1
                # 2. 위쪽 가로 묶기 (조건부)
                if u_arr[i] + u_arr[i - 1] <= W:
                    b[i] = min(b[i], c[i - 1] + 1)

                # --- c[i] 계산 (i번째 열 아래쪽만 채워진 상태) ---
                # 1. 단독 배치 (항상 가능)
                c[i] = a[i - 1] + 1
                # 2. 아래쪽 가로 묶기 (조건부)
                if d_arr[i] + d_arr[i - 1] <= W:
                    c[i] = min(c[i], b[i - 1] + 1)

                # --- a[i] 계산 (i번째 열 위아래 모두 채워진 상태) ---
                # 1. b[i] 상태에서 아래를 단독 채우거나, c[i] 상태에서 위를 단독으로 채우는 경우
                a[i] = min(b[i] + 1, c[i] + 1)
                # 2. 세로로 묶는 경우
                if u_arr[i] + d_arr[i] <= W:
                    a[i] = min(a[i], a[i - 1] + 1)
                # 3. 위쪽, 아래쪽 모두 각각 가로로 묶는 경우
                if u_arr[i] + u_arr[i - 1] <= W and d_arr[i] + d_arr[i - 1] <= W:
                    a[i] = min(a[i], a[i - 2] + 2)

        # ----------------------------------------------------
        # Case 0: 1번과 N번 열이 전혀 연결되지 않은 경우
        # ----------------------------------------------------
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
        ans = min(ans, a[N])

        # ----------------------------------------------------
        # Case 1: 위쪽(안쪽 원) 1번과 N번이 연결된 경우
        # ----------------------------------------------------
        if u[1] + u[N] <= W:
            a, b, c = (
                [float("inf")] * (N + 1),
                [float("inf")] * (N + 1),
                [float("inf")] * (N + 1),
            )
            a[0] = 0
            a[1] = 1
            b[1] = 0  # 위쪽은 N번과 연결되었으므로 여기서 비용 0 처리
            c[1] = float("inf")

            u_temp = u[:]
            u_temp[1] = float("inf")  # 2번이 1번과 중복으로 묶이는 것 방지

            run_dp(a, b, c, u_temp, d)
            ans = min(ans, c[N] + 1)

        # ----------------------------------------------------
        # Case 2: 아래쪽(바깥 원) 1번과 N번이 연결된 경우
        # ----------------------------------------------------
        if d[1] + d[N] <= W:
            a, b, c = (
                [float("inf")] * (N + 1),
                [float("inf")] * (N + 1),
                [float("inf")] * (N + 1),
            )
            a[0] = 0
            a[1] = 1
            b[1] = float("inf")
            c[1] = 0  # 아래쪽은 N번과 연결되었으므로 여기서 비용 0 처리

            d_temp = d[:]
            d_temp[1] = float("inf")  # 2번이 1번과 중복으로 묶이는 것 방지

            run_dp(a, b, c, u, d_temp)
            ans = min(ans, b[N] + 1)

        # ----------------------------------------------------
        # Case 3: 위, 아래 모두 1번과 N번이 연결된 경우
        # ----------------------------------------------------
        if u[1] + u[N] <= W and d[1] + d[N] <= W:
            a, b, c = (
                [float("inf")] * (N + 1),
                [float("inf")] * (N + 1),
                [float("inf")] * (N + 1),
            )
            a[0] = 0
            a[1] = 0  # 위, 아래 모두 연결되었으므로 둘 다 비용 0 처리
            b[1] = float("inf")
            c[1] = float("inf")

            u_temp = u[:]
            d_temp = d[:]
            u_temp[1] = float("inf")
            d_temp[1] = float("inf")

            run_dp(a, b, c, u_temp, d_temp)
            ans = min(ans, a[N - 1] + 2)

        print(ans)


if __name__ == "__main__":
    solve()
