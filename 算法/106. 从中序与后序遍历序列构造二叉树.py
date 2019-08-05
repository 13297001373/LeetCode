# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder):
            val = postorder[-1]
            index = inorder.index(val)
            root = TreeNode(val)
            root.left = self.buildTree(inorder[0:index],postorder[0:index])
            root.right = self.buildTree(inorder[index+1:],postorder[index:-1])
            return root
        else:
            return

def test_function():
    solution = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9, 15, 7, 20, 3]
    root = solution.buildTree(inorder,postorder)

if __name__ == '__main__':
    test_function()