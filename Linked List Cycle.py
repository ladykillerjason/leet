class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:return False
        fast,slow = head,head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                return True
        return False


if __name__ == '__main__':
    s  = Solution()
    head = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(1)
    head.next = p2
    p2.next = p3
    p = head
    while p!=None:
        print(p.val)
        p = p.next

    res = s.hasCycle(head)
    print(res)