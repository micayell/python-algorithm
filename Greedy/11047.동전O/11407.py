n,k=map(int,input().split())
coin_arr=[int(input()) for _ in range(n)]

cnt=0
for coin in sorted(coin_arr,reverse=True):
    if k >= coin:
        cnt+=(k//coin)
        k=k%coin

print(cnt)