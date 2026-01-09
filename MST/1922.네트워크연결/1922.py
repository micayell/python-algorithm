def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px < py:
        p[py] = px
    else:
        p[px] = py


def mst_kruskal(n, edges):
    mst_value = 0

    edges.sort(key=lambda x: x[2])

    cnt = 0
    for a, b, c in edges:
        if find_set(a) != find_set(b):
            union(a, b)
            mst_value += c
            cnt += 1
            if cnt == n - 1:
                break

    return mst_value


n = int(input())
m = int(input())
p = [i for i in range(n + 1)]

edges = [list(map(int, input().split())) for _ in range(m)]


res = mst_kruskal(n, edges)
print(res)
