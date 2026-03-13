# 모든 숫자가 양수이기 때문에 리스트의 시작과 끝을 가리키는 두 개의 포인터를 사용하는 투 포인터 기법이 적합하다.

N, S = map(int, input().split())
num = list(map(int, input().split()))

min_len = 21e8
curr_sum = 0
st = 0

for ed in range(N):
    curr_sum += num[ed]

    while curr_sum >= S:
        if min_len > (ed - st + 1):
            min_len = ed - st + 1
        curr_sum -= num[st]
        st += 1

if min_len == 21e8:
    min_len = 0
    
print(min_len)
