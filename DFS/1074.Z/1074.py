N, r, c = map(int, input().split())


def find(N, r, c):
    if N == 0:
        return 0

    half = 2 ** (N - 1)

    area = half * half

    # 1번째
    if r < half and c < half:
        return find(N - 1, r, c)

    # 2번째
    elif r < half and c >= half:
        return area + find(N - 1, r, c - half)

    # 3번째
    elif r >= half and c < half:
        return 2 * area + find(N - 1, r - half, c)
    # 4번째
    elif r >= half and c >= half:
        return 3 * area + find(N - 1, r - half, c - half)


ans = find(N, r, c)
print(ans)
