N = int(input())
heights = [int(input()) for _ in range(N)]


benchmarking = 0
idx = 0
while len(heights) > 0:
    key = heights[0]

    for i in range(1, len(heights)):
        if heights[i] < key:
            benchmarking += 1
        else:
            break

    heights.pop(0)

print(benchmarking)
