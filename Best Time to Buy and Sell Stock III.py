def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    hold1,hold2=-999999,-999999
    release1,release2=0,0
    for i in prices:
        release2=max(release2,hold2+i)
        hold2=max(hold2,release1-i)
        release1=max(release1,hold1+i)
        hold1=max(hold1,-i)
    return release2




if __name__ == '__main__':

    prices = [7, 1, 5, 3, 6, 4]
    res = maxProfit(prices)
    print(res)