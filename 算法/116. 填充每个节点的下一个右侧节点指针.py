# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next: #非根节点
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root