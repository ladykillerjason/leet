def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices: return 0
    prices = [999999] + prices
    llen = len(prices)
    min_left = prices[0]
    dp = [0 for i in range(llen)]
    for i in range(1, llen):
        dp[i] = max(dp[i - 1], prices[i] - min_left)
        if prices[i] < min_left:
            min_left = prices[i]
    return dp[i]


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    res = maxProfit(prices)
    print(res)
