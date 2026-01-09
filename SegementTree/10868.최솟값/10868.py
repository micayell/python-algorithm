# n,m

# n개의 정수

# m개의 a,b


def init(node, st, ed):
    if st == ed:
        tree[node] = arr[st]
        return tree[node]
    mid = (st + ed) // 2
    tree[node] = min(init(node * 2, st, mid), init(node * 2 + 1, mid + 1, ed))
    return tree[node]


def query(node, st, ed, left, right):
    if left > ed or right < st:
        return 21e8

    if left <= st and right >= ed:
        return tree[node]
    mid = (st + ed) // 2
    return min(
        query(node * 2, st, mid, left, right),
        query(node * 2 + 1, mid + 1, ed, left, right),
    )


n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

tree = [0] * (4 * n)

init(1, 0, n - 1)

for i in range(m):
    a, b = map(int, input().split())

    print(query(1, 0, n - 1, a - 1, b - 1))
