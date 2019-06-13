class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return
        pre = head
        p = pre.next
        n = 1
        while p!=None:
            pre = p
            p = pre.next
            n+=1
        pre.next = head
        start = n - (k-1)%n-1
        while start>0:
            start -= 1
            head = head.next
            pre = pre.next
        pre.next = None
        return head

def test_fucntion():
    solution = Solution()
    head = ListNode(-1)
    p = head
    for i in range(3):
        node = ListNode(i)
        p.next = node
        p = p.next
    head = head.next
    p = head
    while p!=None:
        print(str(p.val)+str('->'),end='')
        p = p.next

    k = 4
    head = solution.rotateRight(head,k)
    p = head
    print()
    while p!=None:
        print(str(p.val)+str('->'),end='')
        p = p.next

if __name__ == '__main__':
    test_fucntion()

