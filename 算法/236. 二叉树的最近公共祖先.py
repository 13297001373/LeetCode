class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findElement(root,p,q):
            if root:
                if root.val == p.val or root.val == q.val:
                    return True
                return findElement(root.left,p,q) or findElement(root.right,p,q)
            return False

        if root:
            item = 0
            if root.val == p.val or root.val == q.val:
                item = 1
            left = 1 if findElement(root.left,p,q) else 0
            right = 1 if findElement(root.right,p,q) else 0
            if left+right+item>=2:
                return root
            if left:
                return self.lowestCommonAncestor(root.left,p,q)
            if right:
                return self.lowestCommonAncestor(root.right,p,q)
        return None