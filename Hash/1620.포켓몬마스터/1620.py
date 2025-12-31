# 포켓몬 개수, 문제의 개수

# 포켓몬 이름들

# 문제들

n,m=map(int,input().split())
pocketmons=[input() for _ in range(n)]
quiz=[input() for _ in range(m)]

for q in quiz:
    if q in pocketmons:
        print(pocketmons.index(q)+1)
    else:
        print(pocketmons[int(q)-1])