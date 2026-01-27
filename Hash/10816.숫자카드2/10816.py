N = int(input())
given = list(map(int, input().split()))
M = int(input())
to_find = list(map(int, input().split()))
for a in to_find:
    print(given.count(a), end=" ")
