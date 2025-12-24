N=int(input())
arr=list(int(input()) for _ in range(N))

# 원래는 pop(0) 사용했는데 l, r로 인덱싱 함
def merge(left,right):
    result=[]

    l=0
    r=0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    
    result.extend(left[l:])
    result.extend(right[r:])

    return result

def merge_sort(arr):
    n=len(arr)

    if n<=1:
        return arr
    
    mid = n//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

res = merge_sort(arr)

for i in res:
    print(i)