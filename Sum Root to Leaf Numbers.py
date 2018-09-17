class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        return self.dfs(root,0)

    def dfs(self,root,tmp):
        if not root:return 0
        tmp = tmp*10+root.val
        if not root.left and not root.right:return tmp
        return self.dfs(root.left,tmp)+self.dfs(root.right,tmp)



if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.right.right = TreeNode(6)
    res = s.sumNumbers(root)
    print(res)