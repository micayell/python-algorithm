# 수의 개수, 수의 변경이 일어나는 횟수, 구간의 합을 구하는 횟수

# n개의 수가 주어짐

# a,b,c
# a가 1인 경우 b번째 수를 c로 바꾸고
# a가 2인 경우 b번째 수부터 c번째 수까지의 합을 구하여 출력

n, m, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

for _ in range(m + k):
    res = 21e8
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b - 1] = c
    elif a == 2:
        res = sum(arr[b - 1 : c])

    if res != 21e8:
        print(res)
