# Definition for singly-linked list.
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
        node = head
        li = []
        while node:
            li.append(node.val)
            node = node.next
        li.sort()
        def genListNode(l):
            start = ListNode(0)
            cur = start
            for i in l:
                cur.next = ListNode(i)
                cur = cur.next
            return start.next
        return genListNode(li)