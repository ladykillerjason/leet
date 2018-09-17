def numDistinct(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    sl,tl = len(s),len(t)
    dp=[[0 for j in range(sl+1)] for i in range(tl+1)]
    for i in range(sl+1):dp[0][i]=1
    for i in range(1,tl+1):dp[i][0]=0
    for i in range(1,tl+1):
        for j in range(1,sl+1):
            dp[i][j]= dp[i][j-1]+(dp[i-1][j-1] if t[i-1]==s[j-1] else 0)
    return dp[i][j]

if __name__ == '__main__':
    S = "rabbbit"
    T = "rabbit"
    res = numDistinct(S,T)
    print(res)