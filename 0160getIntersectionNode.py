# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        flag = 0
        if not (headA and headB):
            return None

        while(a!=b):
            if a.next:
                a = a.next
            else:
                a = headB
                flag = flag + 1
            b = b.next if b.next else headA
            if flag == 2:
                a = None
                break
        return a