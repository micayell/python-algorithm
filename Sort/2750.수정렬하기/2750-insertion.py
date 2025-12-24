def insertion_sort(arr):
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

n=int(input())
arr=list(int(input()) for _ in range(n))

insertion_sort(arr)
for i in arr:
    print(i)