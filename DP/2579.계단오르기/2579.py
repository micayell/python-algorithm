n=int(input())
stairs_point=[]
for _ in range(n):
    stairs_point.append(int(input()))

dp=[0]*(n+1)

def solve(n):
    dp[1]=stairs_point[0]
    dp[2]=stairs_point[0]+stairs_point[1]

    for i in range(3,n+1):
        dp[i]=max(dp[i-3]+stairs_point[i-2]+stairs_point[i-1], dp[i-2]+stairs_point[i-1])

    return dp[n]
if n<=2:
    print(sum(stairs_point))
else:
    print(solve(n))

