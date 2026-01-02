# 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다.
# 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.
# 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다.

import sys
input=sys.stdin.readline
sys.setrecursionlimit(20000)

preorder_arr=[]
while 1:
    try:
        preorder_arr.append(int(input()))
    except:
        break

def pre_to_post(arr):
    if not arr:
        return

    key=arr[0]
    division_idx=len(arr)

    for i in range(1,len(arr)):
        if arr[i] > key:
            division_idx=i
            break
    
    left_arr=arr[1:division_idx]
    right_arr=arr[division_idx:]

    pre_to_post(left_arr)
    pre_to_post(right_arr)

    print(key)

pre_to_post(preorder_arr)