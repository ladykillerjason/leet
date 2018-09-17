class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root: return None
        res = []
        self.dfs(root, sum, res, [])
        return res

    def dfs(self, root, sum, res, path):
        path.append(root.val)
        if not root.left and not root.right and root.val == sum:newPath= [i for i in path];res.append(newPath)
        if root.left:
            self.dfs(root.left, sum-root.val, res, path)
            path.pop()
        if root.right:
            self.dfs(root.right, sum-root.val, res, path)
            path.pop()

    # def dfs(self, root, sum, res, path):
    #     if not root.left and not root.right and root.val == sum:
    #         path.append(root.val)
    #         res.append(path)
    #     if root.left: self.dfs(root.left, sum - root.val, res, path + [root.val])
    #     if root.right: self.dfs(root.right, sum - root.val, res, path + [root.val])

def createTree(arr,index):
    if not arr:return None
    if index<len(arr) and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left=createTree(arr,2*index+1)
        root.right=createTree(arr,2*index+2)
        return root



if __name__=="__main__":
    sol = Solution()
    root = createTree([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1],0)
    # print(root.right.right.left.val)
    res = sol.pathSum(root,22)
    print(res)