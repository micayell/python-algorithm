import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(current_dir,'input.txt'),'r')

def dfs(idx,count,total):
    global result
    if total <= result:
        return
    
    if idx == N or count == N:
        result = max(total, result)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i]=1
            dfs(idx+1, count+1,total*arr[idx][i]*0.01)
            visited[i]=0


T=int(input())
for t in range(1, T+1):
    N=int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    visited = [0 for _ in range(N)]
    dfs(0,0,1)

    print(f'#{t} {result*100:.6f}')