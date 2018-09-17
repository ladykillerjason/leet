class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    l = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        return self.l

    def dfs(self,root):
        if root:
            self.l.append(root.val)
            self.dfs(root.left)
            self.dfs(root.right)



    def preorderTraversal1(self, root):
        ll = []
        stack = []
        while root:
            ll.append(root.val)
            if root.right:stack.append(root.right)
            root = root.left
            if not root and stack:root = stack.pop()
        return ll

if __name__ == '__main__':

    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # root = None
    res = s.preorderTraversal1(root)
    print(res)