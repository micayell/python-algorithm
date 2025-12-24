def bubble_sort(arr):
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))


bubble_sort(arr)
for i in arr:
    print(i)