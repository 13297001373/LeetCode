# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums):
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root
        else:
            return

def test_function():
    solution = Solution()
    nums = [-10,-3,0,5,9]
    root = solution.sortedArrayToBST(nums)

if __name__ == '__main__':
    test_function()