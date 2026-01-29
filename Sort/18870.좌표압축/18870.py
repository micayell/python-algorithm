N = int(input())

X_arr = list(map(int, input().split()))
temp_arr = sorted(set(X_arr))
dict = {}
for i, x in enumerate(temp_arr):
    dict[x] = i

ans = [dict[x] for x in X_arr]

print(*ans)
