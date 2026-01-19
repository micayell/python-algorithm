order = list(map(int, input().split()))

arr = [1, 2, 3, 4, 5, 6, 7, 8]
if order == arr:
    print("ascending")
elif order == sorted(arr, reverse=-1):
    print("descending")
else:
    print("mixed")
