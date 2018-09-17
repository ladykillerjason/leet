# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, temp, stack, flag=[], [], [root], 1
        while stack:
            for i in range(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res

def get_binary_tree(input):
    while input:
        root = TreeNode(input.pop(0))
        root.left=TreeNode(input.pop(0))
        root.right=TreeNode(input.pop(0))


if __name__ =="__main__":
    input  = [3,9,20,None,None,15,7]
    root = get_binary_tree(input)
    # solution = Solution()
    # res = solution.zigzagLevelOrder(root)
    # print(res)