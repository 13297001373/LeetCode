# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def Tracer(root,sum,res):
            if not root:
                return
            if not root.left and not root.right and sum-root.val == 0:
                answer.append(res+[root.val])
                return
            Tracer(root.left,sum-root.val,res+[root.val])
            Tracer(root.right,sum-root.val,res+[root.val])
        answer = []
        Tracer(root,sum,[])
        return answer
        print(answer)

def test_function():
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(4)
    sum = 9
    solution.pathSum(root,sum)

if __name__ == '__main__':
    test_function()


