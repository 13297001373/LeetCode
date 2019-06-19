class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #  a+y+ b = b+y+ a
        p,q = headA,headB
        while p!=q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

def test_function():
    solution = Solution()
    solution.getIntersectionNode(headA,headB)

if __name__ == '__main__':
    test_function()

