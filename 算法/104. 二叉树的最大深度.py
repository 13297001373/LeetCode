class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            left = self.maxDepth(root.left)+1
            right = self.maxDepth(root.right)+1
            return left if left>right else right

def test_function():
    solution = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)

    res = solution.maxDepth(root)
    print(res)

if __name__ == '__main__':
    test_function()