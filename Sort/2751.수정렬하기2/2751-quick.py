n=int(input())
arr=list(int(input()) for _ in range(n))

def quick_sort(arr, st, ed):
    if st < ed:
        p = partition(arr, st, ed)

        quick_sort(arr, st, p-1)
        quick_sort(arr, p+1, ed)


def partition(arr, st, ed):
    p=arr[st]
    left=st+1
    right=ed

    while True:
        while left <= ed and arr[left] < p:
            left+=1

        while right > st and arr[right] >= p:
            right-=1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

        else:
            break

    arr[st], arr[right] = arr[right], arr[st]

    return right

quick_sort(arr,0,n-1)
for i in arr:
    print(i)