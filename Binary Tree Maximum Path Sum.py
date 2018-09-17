class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    maxv = -999999
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.maxv

    def dfs(self,root):
        if not root:return 0
        left = max(0,self.dfs(root.left))
        right = max(0,self.dfs(root.right))
        self.maxv = max(self.maxv,left+right+root.val)
        return max(left,right)+root.val


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    res = s.maxPathSum(root)
    print(res)