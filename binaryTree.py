# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        index= inorder.index(root.val)
        root.left= self.buildTree(preorder,inorder[:index])
        root.right= self.buildTree(preorder, inorder[index+1:])
        return root

if __name__ == '__main__':
    solution = Solution()
    preorder = [1,2,4,5,3,6,7]
    inorder = [4,2,5,1,6,3,7]
    root = solution.buildTree(preorder,inorder)
    print(root.left.left.val)