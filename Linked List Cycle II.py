class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:None
        fast,slow = head,head
        flag = False
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                flag = True
                break
        if not flag:return None
        p = head
        while p!=fast:
            p= p.next
            fast = fast.next
        return p


if __name__ == '__main__':
    s  = Solution()
    head = ListNode(1)
    p2 = ListNode(2)
    p3 = ListNode(3)
    p4 = ListNode(4)
    head.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p2
    # p = head
    # while p!=None:
    #     print(p.val)
    #     p = p.next

    res = s.detectCycle(head)
    print(res.val)