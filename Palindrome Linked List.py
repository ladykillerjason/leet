class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """



if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    p = head
    for i in range(2, 6):
        temp = ListNode(i)
        p.next = temp
        p = temp

    res = s.isPalindrome()
    print(res)
