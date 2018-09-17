class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return None
        if len(nums)==1:
            return nums[0]
        left = 0
        right = len(nums)-1
        return self.fun(nums,left,right)


    def fun(self,nums,left,right):
        if right-left==1:
            return min(nums[left],nums[right])
        mid = (left+right) // 2
        if nums[mid] > nums[right]:
            left = mid
            return self.fun(nums, left, right)
        elif nums[mid] < nums[right]:
            right = mid
            return self.fun(nums,left,right)
        else:
            return self.fun(nums,left,right-1)



if __name__ == '__main__':
    s = Solution()
    nums = [3,3,1,3]
    res = s.findMin(nums)
    print(res)