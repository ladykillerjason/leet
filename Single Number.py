class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,2,3]
    res = s.singleNumber(nums)
    print(res)
    # print(0^312)