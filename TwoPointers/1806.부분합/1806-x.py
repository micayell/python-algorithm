# 모든 숫자가 양수이기 때문에 리스트의 시작과 끝을 가리키는 두 개의 포인터를 사용하는 투 포인터 기법이 적합하다.

N, S = map(int, input().split())
num = list(map(int, input().split()))

min_len = 21e8
curr_sum = 0
st, ed = 0, 0

while 1:
    curr_sum = sum(num[st : ed + 1])

    if curr_sum >= S:
        if min_len > (ed - st + 1):
            min_len = ed - st + 1
        st += 1
    elif ed == N:
        if curr_sum < S:
            if min_len == 21e8:
                min_len = 0
            break
    else:
        ed += 1

print(min_len)
