# N의 최댓값이 1,000,000,000(10억)이기 때문에, 1부터 N까지 반복문을 돌며 문자열로 변환해 개수를 세는 O(N) 방식으로는 무조건 시간 초과가 발생합니다.
N = int(input())

ans = [0] * 10
start = 1
end = N
point = 1  # 자릿수 가중치


def calc(x, point):
    while x > 0:
        ans[x % 10] += point
        x = x // 10


while start <= end:
    # 1. start의 일의 자리를 0으로 맞추기
    while (start % 10 != 0) and (start <= end):
        calc(start, point)
        start += 1

    if start > end:
        break

    # 2. end의 일의 자리를 9로 맞추기
    while (end % 10 != 9) and (start <= end):
        calc(end, point)
        end -= 1

    # 3. 0~9가 한 세트로 묶이는 횟수를 구하여 일괄 합산
    fre = (end // 10) - (start // 10) + 1  # 세트 반복 횟수
    for i in range(0, 10):
        ans[i] += fre * point

    # 4. 다음 자릿수(십, 백, 천 ...)로 이동
    start = start // 10
    end = end // 10
    point = point * 10

print(*ans)
