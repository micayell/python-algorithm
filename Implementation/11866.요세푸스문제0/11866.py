N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
res = []
cnt = 0
idx = 0

while len(res) < N:
    if arr[idx] != 0:
        cnt += 1
        if cnt == K:
            res.append(arr[idx])
            arr[idx] = 0
            cnt = 0
    idx = (idx + 1) % N

answer = "<" + ", ".join(map(str, res)) + ">"
print(answer)