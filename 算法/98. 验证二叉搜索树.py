# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''中序遍历'''
        def tracker(root):
            if root:
                tracker(root.left)
                res.append(root.val)
                tracker(root.right)
            else:
                return
        res = []
        tracker(root)
        return res == sorted(res) and len(set(res))==len(res)
    def isValidBST(self,root):
        def isTrue(root,MIN,MAX):
            if root:
                if MIN>=root.val or MAX<=root.val:
                    return False
                return isTrue(root.left,MIN,root.val) and self.isValidBST(root.right,root.val,MAX)
            else:
                return True
        MIN = float(-Inf)
        MAX = float(Inf)
        return isTrue(root,MIN,MAX)

