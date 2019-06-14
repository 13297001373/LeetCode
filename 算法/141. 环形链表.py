class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while 1:
            try:
                fast = fast.next.next
                slow = slow.next
                if fast.val == slow.val:
                    return True
            except Exception:
                return False
def test_function():
    solution = Solution()
    head = ListNode(0)
    p = head
    for i in range(3):
        p.next = ListNode(i+1)
        p = p.next
    #p.next = head
    res = solution.hasCycle(head)
    print(res)

if __name__ == '__main__':
    test_function()

