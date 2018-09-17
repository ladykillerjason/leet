class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        if left>right:return []
        output = []
        for i in range(left,right+1):
            if self.fun(i):
                output.append(i)
        return output



    def fun(self,no):
        si = str(no)
        if si.__contains__('0'):
            return False
        else:
            for j in si:
                if no % int(j)!=0:
                    return False
            return True


if __name__ == '__main__':
    s = Solution()
    res = s.selfDividingNumbers(1,22)
    print(res)