N = int(input())
# control = ["push", "pop", "size", "empty", "front", "back"]

arr = []
for _ in range(N):
    S = input()
    if "push" in S:
        arr.append(int(S[5:]))
    if "pop" == S:
        if len(arr):
            print(arr.pop(0))
        else:
            print(-1)
    if "size" == S:
        print(len(arr))
    if "empty" == S:
        if len(arr):
            print(0)
        else:
            print(1)
    if "front" == S:
        if len(arr):
            print(arr[0])
        else:
            print(-1)
    if "back" == S:
        if len(arr):
            print(arr[-1])
        else:
            print(-1)
