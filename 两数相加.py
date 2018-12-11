# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def append(self,x):
        res = self
        res.val = x
        res = res.next
        return res

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        sum1 = sum2 = 0
        i = j =0
        while l1 :
            tmp = l1.val
            for row in range(i):
                tmp*=10
            sum1+=tmp
            l1 = l1.next
            i+=1
        while l2 :
            tmp = l2.val
            for row in range(j):
                tmp*=10
            sum2+=tmp
            l2 = l2.next
            j+=1
        sum = sum1+sum2
        list = ListNode(sum%10)
        res = list
        while sum >= 10:
            sum = sum//10
            res.next = ListNode(sum%10)
            res = res.next
        res = list
        return res


if __name__ =='__main__':
    solution  = Solution()
    list= solution.addTwoNumbers(list1,list2)

