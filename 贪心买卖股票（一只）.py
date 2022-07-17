def maxProfit(prices):
    return sum([prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] - prices[i] > 0])

prices=[4,1,6,9,5,2]
result=maxProfit(prices)
print(result)


def maxProfit(prices):
    for i in range(len(prices)-1):
        if prices[i +1] >prices[i]:
            return sum(prices[i +1]-prices[i])