from collections import deque

N = int(input())

queue = deque()
queue.extend(range(1, N + 1))

while queue:
    x = queue.popleft()

    if queue:
        y = queue.popleft()
        queue.append(y)

    else:
        print(x)
        break
