# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = 0
        indexs = [] #定义初始每一个list的首下标
        for list in lists:
            while list!=None:
                k+=1
                list = list.next
        count = 0

        res = ListNode(9999)
        p = res
        while count<k:
            min_value = 999999
            for i in range(len(lists)):
                if lists[i]!=None:
                    if lists[i].val<min_value:
                        min_value = lists[i].val
                        index = i

            p.next = ListNode(min_value)
            p = p.next
            if lists[index]!=None:
                lists[index] = lists[index].next
            else:
                del lists[index]
            count+=1
        return res.next

    ##划分为2个链表的合并
    def mergeKLists2(self, lists):
        if len(lists)<1:
            return None
        head = lists[0]
        for i in range(1,len(lists)):
            head = self.mergeTwoLists(head,lists[i])
        return head
    def mergeTwoLists(self,list1,list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val<list2.val:
            head = list1
            head.next = self.mergeTwoLists(list1.next,list2)
        else:
            head = list2
            head.next = self.mergeTwoLists(list1,list2.next)
        return head
    ##暴力求解，遍历所有链表，存值排序，然后进行链表化
    def mergeKLists(self, lists):
        nums = []
        for list in lists:
            while list!=None:
                nums.append(list.val)
                list = list.next
        nums = sorted(nums)
        head = ListNode(9999999999)
        p = head
        for num in nums:
            p.next = ListNode(num)
            p = p.next
        return head.next
def test_function():
    solution = Solution()
    lists = []
    lists.append(ListNode(1))
    lists.append(ListNode(3))
    res = solution.mergeKLists(lists)
    while res!=None:
        print(res.val)
        res = res.next

if __name__ == '__main__':
    test_function()




