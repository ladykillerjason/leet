class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1,max2,max3 = -99999999999,-99999999999,-99999999999
        min1,min2 = 99999999999,99999999999
        for n in nums:
            if n>max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n>max2:
                max3 = max2
                max2 = n
            elif n>max3:
                max3 = n
            if n<min1:
                min2 = min1
                min1 = n
            elif n<min2 and n>=min1:
                min2 = n
        return max(max1*max2*max3,max1*min1*min2)






if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4]
    res = s.maximumProduct(nums)
    print(res)