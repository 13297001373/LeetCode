# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''中序遍历'''
        def Tracer(root):
            if root:
                Tracer(root.left)
                res.append(root.val)
                Tracer(root.right)
            else:
                res.append('null')
        res = []
        Tracer(root)
        i,j = 0,len(res)-1
        while i<j:
            if res[i]==res[j]:
                i+=1
                j+=1
            else:
                break
        return i==j
    def isSymmetric1(self,root):
        def isSame(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isSame(left.left,right.right) and isSame(left.right,right.left)
        return isSame(root,root)