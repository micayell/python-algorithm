T = int(input())

for _ in range(1, T + 1):
    N = int(input())
    stock_value = list(map(int, input().split()))

    buy = []
    sell = []
    income = 0
    for i in range(N - 1):
        if stock_value[i] > stock_value[i + 1]:
            if len(buy):
                sell.append(stock_value[i] * len(buy))
                income += sum(sell) - sum(buy)
                sell = []
                buy = []
        elif stock_value[i] < stock_value[i + 1]:
            buy.append(stock_value[i])
        elif stock_value[i] == stock_value[i + 1]:
            if i + 1 < N and stock_value[i] < max(stock_value[i + 1 :]):
                buy.append(stock_value[i])

    if len(buy):
        sell.append(stock_value[-1] * len(buy))

    income += sum(sell) - sum(buy)
    print(income)
