from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001


def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        curr = queue.popleft()

        if curr == K:
            return visited[curr]

        for next_pos in (curr - 1, curr + 1, curr * 2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == 0:
                queue.append(next_pos)
                visited[next_pos] = visited[curr] + 1


res = bfs()
print(res)
