n=int(input())
m=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]
place=list(map(int,input().split()))
p=[i for i in range(n+1)]

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x,y):
    px=find_set(x)
    py=find_set(y)

    if px == py:
        return
    else:
        if px < py:
            p[py]=px
        else:
            p[px]=py

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            union(i+1,j+1)


flag=1
for k in range(1,m):
    if find_set(place[k]) != find_set(place[0]):
        flag=0
        break

if flag:
    print('YES')
else:
    print('NO')