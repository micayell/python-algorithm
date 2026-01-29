import sys

input = sys.stdin.readline

N, M = map(int, input().split())

heights = sorted(list(map(int, input().split())))

max_v = heights[-1]
min_v = 0


while min_v <= max_v:
    temp = 0

    Half = (min_v + max_v) // 2

    for h in heights:
        if h > Half:
            temp += h - Half

    if temp >= M:
        ans = Half
        min_v = Half + 1
    elif temp < M:
        max_v = Half - 1

print(ans)
