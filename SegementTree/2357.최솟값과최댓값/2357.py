N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]

min_tree = [0] * (N * 4)
max_tree = [0] * (N * 4)


def min_init(node, st, ed):
    if st == ed:
        min_tree[node] = nums[st]
        return min_tree[node]
    mid = (st + ed) // 2
    min_tree[node] = min(
        min_init(node * 2, st, mid), min_init(node * 2 + 1, mid + 1, ed)
    )
    return min_tree[node]


def max_init(node, st, ed):
    if st == ed:
        max_tree[node] = nums[st]
        return max_tree[node]
    mid = (st + ed) // 2
    max_tree[node] = max(
        max_init(node * 2, st, mid), max_init(node * 2 + 1, mid + 1, ed)
    )
    return max_tree[node]


min_init(1, 0, N - 1)
max_init(1, 0, N - 1)


def min_query(node, st, ed, left, right):
    if left > ed or right < st:  # 범위를 벗어났을 때
        return float("inf")
    if left <= st and right >= ed:
        return min_tree[node]
    mid = (st + ed) // 2
    return min(
        min_query(node * 2, st, mid, left, right),
        min_query(node * 2 + 1, mid + 1, ed, left, right),
    )


def max_query(node, st, ed, left, right):
    if left > ed or right < st:
        return 0
    if left <= st and right >= ed:
        return max_tree[node]
    mid = (st + ed) // 2
    return max(
        max_query(node * 2, st, mid, left, right),
        max_query(node * 2 + 1, mid + 1, ed, left, right),
    )


for i in range(M):
    a, b = map(int, input().split())
    print(min_query(1, 0, N - 1, a - 1, b - 1), max_query(1, 0, N - 1, a - 1, b - 1))
