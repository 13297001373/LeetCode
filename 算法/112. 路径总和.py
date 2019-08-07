# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right: #叶子节点
            return sum-root.val == 0
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val) ##非叶子节点

def test_function():
    solution = Solution()
    res = solution.hasPathSum(root,sum)
    print(res)

if __name__ == '__main__':
    test_function()