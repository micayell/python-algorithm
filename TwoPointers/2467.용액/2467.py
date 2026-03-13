N = int(input())
solution = list(map(int, input().split()))
res = 21e8
xy = [0] * 2


def two_pointer(st, ed):
    global res
    while st < ed:
        temp = solution[st] + solution[ed]

        if temp == 0:
            xy[0], xy[1] = solution[st], solution[ed]
            return
        elif temp < 0:
            if res > abs(temp):
                res = abs(temp)
                xy[0], xy[1] = solution[st], solution[ed]
            st += 1
        elif temp > 0:
            if res > temp:
                res = temp
                xy[0], xy[1] = solution[st], solution[ed]
            ed -= 1


two_pointer(0, N - 1)

print(*xy)
