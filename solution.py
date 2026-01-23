N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
k = K
res = []
st = 0
cnt = 1
while 1:
    for i in range(st, len(arr)):
        if cnt % k == 0:
            res.append(arr[i])
            arr[i] = 0
            st = (i + 1) % 7
            break
        if arr[i]:
            cnt += 1

    if len(set(arr)) == 1:
        break

answer = "<" + ", ".join(map(str, res)) + ">"
print(answer)
