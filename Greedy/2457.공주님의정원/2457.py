N = int(input())

st = 301
ed = 1201

arr = []
for _ in range(N):
    st_month, st_day, ed_month, ed_day = map(int, input().split())
    start = st_month * 100 + st_day
    end = ed_month * 100 + ed_day
    arr.append([start, end])

arr.sort(key=lambda x: (x[0], -x[1]))

target = 301
cnt = 0
idx = 0
while target < 1201:
    max_end = 0
    for i in range(idx, len(arr)):
        cur_st, cur_ed = arr[i]
        if cur_st <= target:
            max_end = max(cur_ed, max_end)
            idx += 1

    if max_end:
        target = max_end
        cnt += 1
    else:
        cnt = 0
        break

print(cnt)
