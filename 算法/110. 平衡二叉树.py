# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def Hight(root):
            if root:
                return max(1+Hight(root.left),1+Hight(root.right))
            else:
                return 0
        if root:
            left = Hight(root.left)
            right = Hight(root.right)
            return abs(left-right)<2 and self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return True
    def isBalanced(self,root):
        def Tracer(root):
            if root:
                left = 1+Tracer(root.left)
                right = 1+Tracer(root.right)
                if abs(left-right)>1:
                    flag = False
                return max(left,right)
            else:
                return 0
        flag = True
        Tracer(root)
        return flag



def test_function():
    solution = Solution()
    flag = solution.isBalanced(root)


if __name__ == '__main__':
    test_function()