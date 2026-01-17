T = int(input())

for _ in range(T):
    S = input()
    cnt = 0
    res = 0
    for ss in S:
        if ss == "O":
            cnt += 1
            res += cnt
        else:
            cnt = 0
    print(res)
