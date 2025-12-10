def Calculate(idx, Sum):
    global count
    if idx >= N:
        return
    
    Sum += arr[idx]

    if Sum == S:
        count += 1

    Calculate(idx+1, Sum)
    Calculate(idx+1, Sum - arr[idx])
    
N, S = map(int,input().split())
arr=list(map(int,input().split()))

count = 0

Calculate(0, 0)

print(count)