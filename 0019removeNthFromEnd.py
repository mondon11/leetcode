# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        start = head
        while(head):
            count = count+1
            head = head.next
        if count == 1:
            return None
        if count == n:
            return start.next
        p = 1
        begin = start
        while(p<count-n):
            p = p+1
            begin = begin.next
        begin.next = begin.next.next
        return start

    def removeNthFromEnd1(self, head, n):
        start = head
        fast = head
        slow = head
        tmp = n
        while(n>0):
            fast = fast.next
            n = n-1
        if fast == None:
            return None if tmp == 1 else start.next
        while(fast.next):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return start