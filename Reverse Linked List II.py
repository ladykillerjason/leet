class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummpy=ListNode(11)
        dummpy.next = head
        p = dummpy
        i = 0
        while i<m-1:
            p = p.next
            i+=1
        mpre = p
        while i<n:
            p = p.next
            i+=1
        nnext = p.next
        p = mpre.next.next
        mpre.next.next = nnext
        pre = mpre.next
        while p!=nnext:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        mpre.next = pre
        return dummpy.next

    def reverse1(self,head):
        pre = None
        p = head
        while p != None:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre



if __name__ == '__main__':

    s = Solution()
    head = ListNode(1)
    p=head
    for i in range(2,6):
        temp = ListNode(i)
        p.next = temp
        p=temp
    res = s.reverseBetween(head,2,4)
    # res = s.reverse1(head)
    p = res
    while p !=None:
        print(p.val)
        p = p.next
    # print(head.next.val)