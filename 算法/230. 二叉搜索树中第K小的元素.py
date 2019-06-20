class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int

        """

        def getValue(root):
            if root:
                getValue(root.left)
                res.append(root.val)
                getValue(root.right)
            return
        res = []
        getValue(root)
        return rses[k-1]
def test_function():
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(3)
    k = 2
    res = solution.kthSmallest(root,k)
    print(res)

if __name__ == '__main__':
    test_function()

