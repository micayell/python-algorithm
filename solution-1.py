import sys

input = sys.stdin.readline


def solve():
    T = int(input())

    for _ in range(T):
        N, W = map(int, input().split())
        enemy = [list(map(int, input().split())) for _ in range(2)]

        u = [0] + enemy[0]
        d = [0] + enemy[1]

        if N == 1:
            if u[1] + d[1] <= W:
                print(1)
            else:
                print(2)
            continue

        ans = float("inf")

        def run_dp(a, b, c, u_arr, d_arr):
            for i in range(2, N + 1):
                b[i] = a[i - 1] + 1
                if u_arr[i] + u_arr[i - 1] <= W:
                    b[i] = min(b[i], c[i - 1] + 1)

                c[i] = a[i - 1] + 1
                if d_arr[i] + d_arr[i - 1] <= W:
                    c[i] = min(c[i], b[i - 1] + 1)

                a[i] = min(b[i] + 1, c[i] + 1)
                if u_arr[i] + d_arr[i] <= W:
                    a[i] = min(a[i], a[i - 1] + 1)
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
            b[1] = 0
            c[1] = float("inf")

            u_temp = u[:]
            u_temp[1] = float("inf")

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
            c[1] = 0

            d_temp = d[:]
            d_temp[1] = float("inf")

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
            a[1] = 0
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
