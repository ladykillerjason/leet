def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = list()
    m = dict()
    i = 0
    while i < len(nums):
        if target-nums[i] in m.keys():
            result.append(m[target-nums[i]])
            result.append(i)
            return result
        else:
            m[nums[i]] = i
        i += 1
    return result

nums = [2, 7, 11, 15]
target = 9
res = twoSum(nums=nums, target=target)
# print(res)
# m = dict()
# m[0] = 10
# print(1 in m.keys())

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    l3 = ListNode(0)
    curNode = l3
    while l1 != None or l2 !=None:
        val1 = 0
        if l1 != None:
            val1 = l1.val
            l1 = l1.next
        val2 = 0
        if l2 != None:
            val2 = l2.val
            l2 = l2.next
        value = val1 + val2 + carry
        newNode = ListNode(value % 10)
        curNode.next = newNode
        carry = value // 10
        curNode = curNode.next
    if carry > 0 :
        curNode.next = ListNode(carry)
    return l3.next

l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)
l21 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)

l12.next = l13
l11.next = l12
l22.next = l23
l21.next = l22

l = list()
l[0] = "shit"
print(l)

l = addTwoNumbers(l11, l21)
while l != None:
    print(l.val)
    l = l.next