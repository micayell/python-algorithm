import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
    exit()

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append([c, w])
    tree[c].append([p, w])


def dfs(node):
    dist = [-1] * (n + 1)
    stack = [(node, 0)]
    dist[node] = 0

    max_dist = 0
    farthest_node = node

    while stack:
        curr_node, curr_dist = stack.pop()

        if curr_dist > max_dist:
            max_dist = curr_dist
            farthest_node = curr_node

        for next_node, weight in tree[curr_node]:
            if dist[next_node] == -1:
                dist[next_node] = curr_dist + weight
                stack.append((next_node, curr_dist + weight))

    return farthest_node, max_dist


f_node, _ = dfs(1)
_, diameter = dfs(f_node)
print(diameter)
