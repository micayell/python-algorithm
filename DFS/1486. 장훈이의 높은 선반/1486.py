import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(current_dir,'input.txt'),'r')


def combination(arr, r):
    acc = []
    if r == 1:
        return [[i] for i in arr]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:],r-1):
            acc.append([elem]+rest)
    return acc

T=int(input())
for tc in range(1, T+1):
    N,B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 10000*20+1

    # 완전 검색
    for r in range(1, N+1):
        for comb in combination(arr, r):
            total_height = sum(comb)
            if total_height >= B:
                result = min(total_height, result)

    print(f'#{tc} {result-B}')