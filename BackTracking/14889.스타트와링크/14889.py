n=int(input())
s_arr=[list(map(int,input().split())) for _ in range(n)]

res=21e8
visited=[0]*n

def dfs(level,idx):
    global res

    if level==n//2:
        start_value = 0
        link_value = 0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start_value += s_arr[i][j]
                elif not visited[i] and not visited[j]:
                    link_value += s_arr[i][j]

        res=min(res,abs(start_value-link_value))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i]=1
            dfs(level+1,i+1)
            visited[i]=0

dfs(0,0)
print(res)