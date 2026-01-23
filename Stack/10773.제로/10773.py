K = int(input())
arr = []
for _ in range(K):
    k = int(input())
    if k == 0 and len(arr):
        arr.pop(-1)
    elif k != 0:
        arr.append(k)


print(sum(arr))
