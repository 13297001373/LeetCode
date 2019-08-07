# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        while  root:
            if not root.left:
                root = root.right
            else:
                Lnode = root.left
                while Lnode.right: ##找到左子树的最右节点
                    Lnode = Lnode.right
                Lnode.right = root.right
                root.right = root.left
                root.left = None
                root = root.right



def test_function():
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    solution.flatten(root)

if __name__ == '__main__':
    test_function()



