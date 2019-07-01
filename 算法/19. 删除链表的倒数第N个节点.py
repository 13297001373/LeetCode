class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = head
        end = head
        if not start.next:
            return None
        gap = 0
        while end.next:
            if gap>=n:
                start = start.next
            end = end.next
            gap+=1
        start.next = start.next.next
        return head
def test_function():
    solution = Solution()
    head = ListNode(1)
    p = head
    for i in range(2,6):
        p.next = ListNode(i)
        p = p.next
    n = 2
    res = solution.removeNthFromEnd(head,n)
    while res:
        print(res.val)
        res = res.next

if __name__ == '__main__':
    test_function()
