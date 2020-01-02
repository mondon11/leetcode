# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        li = []
        node = head
        while (node):
            li.append(node.val)
            node = node.next
        li.reverse()

        def genListNode(l):
            start = ListNode(0)
            end = start
            for i in l:
                end.next = ListNode(i)
                end = end.next

            return start.next

        return genListNode(li)

    def reverseList1(self,head):
        # if not head:
        #     return None
        # pre = head
        # cur = head
        # cur = cur.next
        # pre.next = None
        # while(cur):
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp
        # return pre
        pre = None
        cur = head
        while(cur):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList2(self,head):
        if head == None or head.next == None:
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur


