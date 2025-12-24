n=int(input())
arr=list(int(input()) for _ in range(n))
max_value=max(arr)

def counting_sort(arr, max_value):
    count_arr=[0]*(max_value+1)
    result = [0]*n

    for num in arr:
        count_arr[num] += 1

    for i in range(1, max_value+1):
        count_arr[i] += count_arr[i-1]

    for i in range(n-1, -1, -1):
        val = arr[i]
        result[count_arr[val]-1] = val
        count_arr[val] -= 1

    return result

res = counting_sort(arr, max_value)

for i in res:
    print(i)