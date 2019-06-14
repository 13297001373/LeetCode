class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sets = {None}
        while head not in sets:
            sets.add(head)
            head = head.next
        return head

def test_function():
    solution = Solution()
    head = ListNode(0)
    p = head
    for i in range(3):
        p.next = ListNode(i+1)
        p = p.next
    p.next = head.next
    res = solution.detectCycle(head)
    print(res)

if __name__ == '__main__':
    test_function()