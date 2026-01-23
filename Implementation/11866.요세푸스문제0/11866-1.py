from collections import deque

N, K = map(int, input().split())
dq = deque(range(1, N + 1))
res = []

while dq:
    # K-1번 왼쪽으로 회전시키면 K번째 사람이 맨 앞으로 옵니다.
    dq.rotate(-(K - 1))
    # 맨 앞사람을 뽑아서 결과에 추가합니다.
    res.append(dq.popleft())

print(f"<{', '.join(map(str, res))}>")