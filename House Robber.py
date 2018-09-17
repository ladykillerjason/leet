class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        if len(nums)==1:return nums[0]
        if len(nums)==2:return max(nums[0],nums[1])
        dp =[0 for i in range(len(nums))]
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[i]

if __name__ == '__main__':
    s = Solution()
    nums = [0,0]
    res = s.rob(nums)
    print(res)