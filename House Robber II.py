class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        if len(nums)==1:return nums[0]
        if len(nums)==2:return max(nums[0],nums[1])
        if len(nums)==3:return max(nums[0],nums[1],nums[2])

        dp =[0 for i in range(len(nums))]
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        max1 = dp[i]
        dp =[0 for i in range(len(nums))]
        dp[1]=nums[1]
        dp[2]=max(nums[1],nums[2])
        for i in range(3,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        max2 = dp[i]
        return max(max1,max2)

if __name__ == '__main__':
    s = Solution()
    nums = [5,6,3,2,7,4,8,2]
    res = s.rob(nums)
    print(res)