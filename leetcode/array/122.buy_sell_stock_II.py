def maxProfit(prices):

    if not prices:
        return 0

    maxProfit = 0

    min = prices[0]
    i = 1
    while(i < len(prices)):
        if prices[i] <= min:
            min = prices[i]
        # buy.append(min)
            i += 1
            continue
        elif prices[i] > min:
            # buy.append(min)
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            # sell.append(prices[i])
            maxProfit += prices[i] - min

            min = prices[i+1] if i < len(prices) - 1 else prices[i]

        i += 1
    return maxProfit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([1, 2, 3, 4, 5]))
