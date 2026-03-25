import sys

input = sys.stdin.readline


N = int(input())
solution = sorted(list(map(int, input().split())))

res = float(
    "inf"
)  # 문제 조건에서 용액의 각가의 값이 10억인데 조건에 따라 최솟값이 30억이 나올 수 도 있어서 21e8은 21억이다보니 적절하지 않은 초기값임.
res_list = [0] * 3
for i in range(N - 2):
    fix_value = solution[i]

    left = i + 1
    right = N - 1

    while left < right:
        temp = fix_value + solution[left] + solution[right]

        if res > abs(temp):
            res = abs(temp)
            res_list = [fix_value, solution[left], solution[right]]

        if temp < 0:
            left += 1
        elif temp > 0:
            right -= 1
        elif temp == 0:
            print(*res_list)
            sys.exit(0)

print(*res_list)
