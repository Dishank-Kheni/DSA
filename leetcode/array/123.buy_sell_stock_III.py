def maxProfit(prices):

    if not prices:
        return 0
    buy = []
    sell = []
    maxProfit = []

    min = prices[0]
    i = 1
    while(i < len(prices)):
        if prices[i] <= min:
            min = prices[i]
            i += 1
            continue
        elif prices[i] > min:
            buy.append(min)
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            sell.append(prices[i])
            maxProfit.append(prices[i] - min)

            min = prices[i+1] if i < len(prices) - 1 else prices[i]

        i += 1
    print(buy)
    print(sell)
    print(maxProfit)

    return maxProfit[-1]+maxProfit[-2] if len(maxProfit) > 1 else maxProfit[0] if maxProfit else 0


# print(maxProfit([7, 1, 5, 3, 6, 4]))
# print(maxProfit([7, 6, 4, 3, 1]))
# print(maxProfit([1, 2, 3, 4, 5]))
# print(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
# print(maxProfit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))

# 13
