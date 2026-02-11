N = int(input())
pos = []
for _ in range(N):
    x, y = map(int, input().split())
    pos.append((x, y))

total = 0
for i in range(N):
    x1, y1 = pos[i]
    x2, y2 = pos[(i + 1) % N]
    total += x1 * y2 - y1 * x2


dimensions = abs(total) / 2
print("%.1f" % dimensions)
