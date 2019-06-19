class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res = sorted(res)
        head = ListNode(res[0])
        p = head
        for i in range(1,len(res)):
            p.next= ListNode(res[i])
            p = p.next
        return head

def test_function():
    solution = Solution()
    head = ListNode(2)
    p = head
    p.next = ListNode(1)
    head = solution.sortList(head)
    while head!=None:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    test_function()