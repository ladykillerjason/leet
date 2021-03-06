class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while (fast != slow):
            fast = nums[fast]
            slow = nums[slow]
        return slow


if __name__ == '__main__':

    s = Solution()
    # nums = [1,2,3,4,5,3]
    nums = [5,4,2,3,7,4,6,1]
    res = s.findDuplicate(nums)
    print(res)