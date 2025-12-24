# 1. n을 먼저 받습니다.
n = int(input())

# 2. 문제에서 숫자는 10,000 이하라고 했으므로 10,001칸을 준비합니다.
# 이 리스트가 우리가 사용하는 유일한 메모리입니다 (약 0.04MB).
count_arr = [0] * 10001

# 3. [수정] arr에 저장하지 않고, 입력받자마자 바로 개수만 셉니다.
for _ in range(n):
    num = int(input())
    count_arr[num] += 1

# 4. [수정] 누적합을 구하거나 result 리스트를 만들지 않습니다.
# count_arr에 저장된 "숫자 i가 몇 번 나왔나" 정보를 그대로 활용해 출력합니다.
for i in range(10001):
    if count_arr[i] != 0:
        # i라는 숫자가 count_arr[i]번 나왔으므로 그 횟수만큼 반복 출력
        for _ in range(count_arr[i]):
            print(i)