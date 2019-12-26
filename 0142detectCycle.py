# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        a = head
        while(1):
            if a == None:
                return None
            if dic.get(a) is None:
                dic[a] = 1
                a = a.next
            else:
                break
        return a

    def detectCycle1(self, head):
        a = head
        b = head
        if not a:
            return None
        while(1):
            a = a.next.next if a.next else None
            b = b.next

            if a == None:
                return None
            if a == b:
                break
        b = head
        while(a!=b):
            a = a.next
            b = b.next

        return a