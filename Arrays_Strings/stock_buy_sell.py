def stock_buy_sell(arr):
    n = len(arr)
    max_profit = 0
    min = arr[0]
    for i in range(1,n):
        if arr[i] < min:
            min = arr[i]
        else:
            profit = arr[i] - min
            max_profit = max(profit,max_profit)
    return max_profit

    

print(stock_buy_sell([7,2,1,5,6,4,8]))