N = int(input())
given = list(map(int, input().split()))
M = int(input())
to_find = list(map(int, input().split()))

dict = {}
for i in given:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for m in to_find:
    if m in dict:
        print(dict[m], end=" ")
    else:
        print(0, end=" ")
