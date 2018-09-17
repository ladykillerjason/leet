class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = True
        s = set()
        while flag:
            res = 0
            while n/10>0:
                res += (n%10)**2
                n = n//10
            n = res
            if res==1:return True
            if res not in s:s.add(res)
            else:flag = False
        return False

if __name__ == '__main__':
    n = 19
    sol = Solution()
    res = sol.isHappy(n)
    print(res)