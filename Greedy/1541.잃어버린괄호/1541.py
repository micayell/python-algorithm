arr=input().split('-')

num=[]
for i in arr:
    k=0
    # if '+' in i:
    temp=i.split('+')
    for j in temp:
        k+=int(j) 
    num.append(k)

res=int(num[0])
for i in range(1,len(num)):
    res-=num[i]

print(res)