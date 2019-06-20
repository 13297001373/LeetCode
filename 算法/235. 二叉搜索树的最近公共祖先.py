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
        if p.val>q.val:
            p,q = q,p
        if root :
            if p.val<=root.val<=q.val:
                return root
            elif p.val<root.val and q.val<root.val:
                return self.lowestCommonAncestor(root.left,p,q)
            else:
                return self.lowestCommonAncestor(root.right,p,q)
        return root
def test_function():
    solution = Solution()
    root = TreeNode(6)
    left2 = TreeNode(2)
    right2 = TreeNode(8)
    root.left = left2
    root.right = right2
    left2.left = TreeNode(0)
    right3 = TreeNode(4)
    left2.right = right3
    right2.left = TreeNode(7)
    right2.right = TreeNode(9)
    right3.left = TreeNode(3)
    right3.right = TreeNode(5)
    p = 2
    q = 4
    res = solution.lowestCommonAncestor(root,TreeNode(2),TreeNode(4))
    print(res.val)

if __name__ == '__main__':
    test_function()
