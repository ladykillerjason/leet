class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==0:return 0
        a = abs(dividend)
        b = abs(divisor)
        counter = 0
        sum = 0
        while sum<=a:
            sum +=b
            counter += 1
        counter -= 1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            return -counter
        else:
            return counter



if __name__ == '__main__':
    s = Solution()
    res = s.divide(1,1)
    print(res)