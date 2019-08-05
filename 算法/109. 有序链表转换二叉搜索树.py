# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def createTree(res):
            if len(res):
                mid = len(res) // 2
                root = TreeNode(res[mid])
                root.left = createTree(res[:mid])
                root.right = createTree(res[mid+1:])
                return root
            else:
                return
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return createTree(res)


def test_function():
    solution = Solution()
    root = solution.sortedListToBST(head)

if __name__ == '__main__':
    test_function()





