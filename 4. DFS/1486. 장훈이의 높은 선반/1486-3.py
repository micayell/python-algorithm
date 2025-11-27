import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(current_dir,'input.txt'),'r')


def dfs(idx,count,total):
    global result
    if total >= B:
        result = min(total, result)
        return
    if idx == N or count == N:
        return
    # 경우 1: 현재 점원(idx)을 포함하는 경우 (키를 더함)
    dfs(idx+1,count+1,total+arr[idx])
    # 경우 2: 현재 점원(idx)을 포함하지 않는 경우 (키 안 더함)
    dfs(idx+1,count,total)

T=int(input())
for tc in range(1, T+1):
    N,B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 10000*20+1

    dfs(0,0,0)

    print(f'{tc} {result-B}')