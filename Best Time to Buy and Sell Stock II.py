def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:return 0
    prices = [99999999]+prices
    llen = len(prices)
    prices = prices+[-99999999]
    dp = [0 for i in range(llen)]
    buy,sell = -1,-1
    for i in range(1,llen):
        if prices[i]<=prices[i-1] and prices[i]<=prices[i+1]:
            buy = prices[i]
        if prices[i]>prices[i-1] and prices[i]>=prices[i+1] and buy>=0: # 必须大于左侧
            sell = prices[i]
            dp[i]=dp[i-1]+sell-buy
        else:
            dp[i]=dp[i-1]
    return dp[i]




if __name__ == '__main__':


    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [2,2,5]
    prices = [5,2,3,2,6,6,2,9,1,0,7,4,5,0]
    res = maxProfit(prices)
    print(res)