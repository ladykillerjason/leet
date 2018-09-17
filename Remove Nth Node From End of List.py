# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        while n >= 0:
            if fast != None:
                fast = fast.next
            n -= 1
        # edge case, i.e if you need to delete the first node itself
        if fast == None:
            dummy.next = dummy.next.next
            return dummy.next

        while fast != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head



if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = s.removeNthFromEnd(head,2)
    print(head.next.next.next.val)