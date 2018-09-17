class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        if num<=0:
            return False
        sum = 1
        for i in range(2,math.floor(math.sqrt(num))+1):
            if num%i==0:
               sum+=i+num/i
        if sum==num:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkPerfectNumber(-6))