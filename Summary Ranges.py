class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:return []
        if len(nums) == 1: return [str(nums[0])]
        nums = nums+[-999999999999999]
        res = []
        start = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if i-1==start:
                    res.append(str(nums[i-1]))
                else:
                    res.append(str(nums[start])+"->"+str(nums[i-1]))
                start = i
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [0,2,3,4,6,8]
    res = s.summaryRanges(nums)
    print(res)