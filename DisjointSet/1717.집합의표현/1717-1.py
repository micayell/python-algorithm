n,m = map(int,input().split())

p=[i for i in range(n+1)]
rank = [0]*(n+1)

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x]

def union(x,y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1

for _ in range(m):
    op, a, b = map(int,input().split())

    if op == 0:
        union(a,b)
    elif op == 1:
        if find_set(a)==find_set(b):
            print('yes')
        else:
            print('no')
