class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)
        p = head
        while l1 and l2:
            if l1.val<l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        ListNode.__lt__ = lambda self, n2: self.val < n2.val
        heap = []
        k = len(lists)
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap,lists[i])
        p = head = ListNode(-1)
        while heap:
            p.next = heapq.heappop(heap)
            p = p.next
            if p.next:
                heapq.heappush(heap,p.next)
        return head.next


def showList(head):
    p = head
    while p:
        print(p.val)
        p = p.next


if __name__ == '__main__':
    s = Solution()
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)
    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    c = ListNode(2)
    c.next = ListNode(6)
    lists = []
    lists.extend([a,b,c])
    newList = s.mergeKLists(lists)
    showList(newList)