class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirror(root):
    if not root:return None
    stack = [root]
    while stack:
        root = stack.pop()
        if root:
            stack.append(root.left)
            stack.append(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp


def mirror_rec(root):
    if not root:return None
    t = root.left
    root.left = root.right
    root.right = t
    mirror_rec(root.left)
    mirror_rec(root.right)


if __name__ == '__main__':
    from pprint import pprint
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    # mirror(root)
    mirror_rec(root)
    print(root.left.left.val)
    print(root.right.left.val)