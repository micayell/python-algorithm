N = int(input())
# W[i][j] : 도시 i에서 j로 가기 위한 비용
W = [list(map(int, input().split())) for _ in range(N)]

all_visited = (1 << N) - 1
dp = [[-1] * (1 << N) for _ in range(N)]
# print(dp)


def dfs(curr_city, visited):
    print(f"-> 현재 위치: {curr_city}번 도시, 방문 상태: {bin(visited)}")
    if visited == all_visited:
        if W[curr_city][0] > 0:
            print(f"  [경로 완성] 0번으로 돌아가는 비용: {W[curr_city][0]}")
            return W[curr_city][0]
        else:
            print("  [경로 실패] 0번으로 돌아가는 길 없음")
            return float("inf")

    if dp[curr_city][visited] != -1:
        print(f"  [메모장 적중] dp[{curr_city}][{visited}] 값 재사용")
        return dp[curr_city][visited]

    min_cost = float("inf")

    for next_city in range(N):
        if W[curr_city][next_city] == 0:
            continue
        # 겹치는 1이 하나도 없으면(방문한 도시가 아니면) 결과는 무조건 0
        if visited & (1 << next_city) != 0:
            continue
        next_visited = visited | (1 << next_city)
        print(
            f"    탐색: {curr_city}번 -> {next_city}번 (다음 상태: {bin(next_visited)})"
        )
        cost = W[curr_city][next_city] + dfs(next_city, next_visited)
        print(f"      [비용 계산] {curr_city}번 -> {next_city}번 이동({W[curr_city][next_city]}) + 남은 최소 비용 = 총 {cost}")

        if cost < min_cost:
            min_cost = cost
            # 6. 최솟값 갱신 확인 프린트 추가
            print(f"      [최솟값 갱신] 현재 {curr_city}번 도시의 최소 비용: {min_cost}")

    dp[curr_city][visited] = min_cost
    return min_cost


answer = dfs(0, 1)
print(answer)
