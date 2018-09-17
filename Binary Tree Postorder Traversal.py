class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def preorderTraversal(self,root):  # 先序   根左右
        ll = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                ll.append(root.val)
                root = root.left
            root = stack.pop().right
        return ll

    def midorderTraversal(self,root):  # 中序   左根右
        ll = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            ll.append(stack[-1].val)
            root = stack.pop().right

        return ll


    #****************************精彩的 后序遍历**************************************


    def postorderTraversal(self, root):  # 后序  左右根
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ll = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                ll=[root.val]+ll
                root = root.right
            else:
                root = stack.pop().left
        return ll

    def postorderTraversal2(self, root):  # 后序2  左右根  (与先序遍历很像，原因值得深思，哈哈哈哈呵呵哈哈哈)
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ll = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                ll=[root.val]+ll
                root = root.right
            root = stack.pop().left
        return ll


    def postorderTraversal3(self, root):  # 后序3  左右根 ,错误的方法
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ll = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack[-1].right
            if not root:
                ll.append(stack.pop().val)
                root = stack[-1].right
        return ll



if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    # root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    # root = None
    res = s.postorderTraversal(root)
    # res = s.postorderTraversal3(root)
    # res = s.preorderTraversal(root)
    # res = s.midorderTraversal(root)
    print(res)