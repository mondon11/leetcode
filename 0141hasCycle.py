# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = head
        b = head
        if not a:
            return False
        while(1):
            a = a.next.next if a.next else None
            b = b.next
            if a == None:
                return False
            if a == b:
                return True