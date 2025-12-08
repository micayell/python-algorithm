import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(current_dir,'input.txt'),'r')

T=int(input())
for tc in range(1, T+1):
    N,B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 10000*20+1

    for i in range(1, 2**N):
        height = 0
        for j in range(N):
            if i & (1 << j):
                height += arr[j]
        # 모든 요소에 대해서 i번째 경우의 수를 다 구했다면
        if height >= B:
            result = min(height, result)

    print(f'{tc} {result - B}')