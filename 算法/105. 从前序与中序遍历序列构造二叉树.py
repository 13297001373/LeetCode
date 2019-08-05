# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder):
            val = preorder[0]
            root = TreeNode(val)
            index = inorder.index(val)
            root.left = self.buildTree(preorder[1:index+1],inorder[0:index])
            root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
            return root
        else:
            return

def test_function():
    solution = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = solution.buildTree(preorder,inorder)

if __name__ == '__main__':
    test_function()