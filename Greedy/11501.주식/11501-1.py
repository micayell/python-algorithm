T = int(input())

for _ in range(1, T + 1):
    N = int(input())
    stock_value = list(map(int, input().split()))

    highest_price = stock_value[-1]
    income = 0
    for i in range(N - 1, -1, -1):
        highest_price = max(highest_price, stock_value[i])
        income += highest_price - stock_value[i]

    print(income)
