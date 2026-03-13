Customer, city = map(int, input().split())

info = []
for _ in range(city):
    cost, n = map(int, input().split())
    info.append((cost, n))

dp = [21e8] * (Customer + 101)
dp[0] = 0
for cost, people in info:
    for i in range(people, Customer + 101):
        dp[i] = min(dp[i], dp[i - people] + cost)

print(min(dp[Customer:]))
