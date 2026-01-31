def recur(start, res):
    if len(res) == M:
        print(*res)
        return

    for i in range(start, N + 1):
        res.append(i)  # 리스트에 추가
        recur(i + 1, res)  # 다음 단계 진행
        res.pop()  # 다시 돌아와서 마지막 원소 제거 (백트래킹)


N, M = map(int, input().split())
recur(1, [])
