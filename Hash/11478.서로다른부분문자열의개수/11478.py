S=input()

n=len(S)
arr=[]
res=''
visited=[0]*n

def dfs(level, res):
    if level == n:
        return
    
    for i in range(level+1):
        if visited[i]==0:
            visited[i]=1
            res+=S[i]
            arr.append(res)
            dfs(i,res)
            visited[i]=0
            res-=S[i]
dfs(0,res)
print(len(set(arr)))
