N, M = map(int, input().split())

res = []


def recur(idx, res):
    if len(res) == M:
        print(*res)
        res = []
        return

    for i in range(idx, N + 1):
        recur(i + 1, res + [i])


recur(1, [])
