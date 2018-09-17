class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        maxx,imax,imin = -999999,1,1
        for i in range(len(nums)):
            if nums[i]<0:imax,imin = imin,imax
            imax = max(imax*nums[i],nums[i])
            imin = min(imin*nums[i],nums[i])
            maxx = max(maxx,imax)
        return maxx


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,-2,4,5,-3]
    res = s.maxProduct(nums)
    print(res)