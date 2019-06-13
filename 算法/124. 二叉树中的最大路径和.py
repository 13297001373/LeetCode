class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def __init__(self):
        self.res = -9999
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findmax(root)
        return self.res
    def findmax(self,root):
        if root == None:
            return 0
        else:
            left = max(0,self.findmax(root.left))
            right = max(0,self.findmax(root.right))
            self.res = max(root.val + left + right, self.res)
            return max(left,right,left+right) + root.val
def test_function():
    solution = Solution()
    root = TreeNode(-2)
    root.left = TreeNode(-1)
    # root.right = TreeNode(3)
    res = solution.maxPathSum(root)
    print(res)

if __name__ == '__main__':
    test_function()
