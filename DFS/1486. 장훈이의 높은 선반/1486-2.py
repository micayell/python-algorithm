import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(current_dir,'input.txt'),'r')


from itertools import combinations

T=int(input())
for tc in range(1, T+1):
    N,B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 10000*20+1

    for r in range(1,len(arr)+1):
        for comb in combinations(arr,r):
            total_height = sum(comb)
            if total_height >= B:
                result = min(total_height, result)

    print(f'#{tc} {result - B}')