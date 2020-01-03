# coding = utf-8
# Definition for singly-linked list.
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
        li = []
        while(head):
            li.append(head.val)
            head = head.next
        #print(li)
        lth = len(li)
        tmp = [0 for _ in range(lth)]
        #print(tmp)
        for i in range(lth):
            j = (i+k)%lth
            tmp[j] = li[i]
        #print(tmp)
        return self.genListNode(tmp)

    def genListNode(self,l):
        head = ListNode(0)
        cur = head
        for item in l:
            cur.next = ListNode(item)
            cur = cur.next
        return head.next

    def rotateRight1(self, head, k):
        if not head:
            return None
        head_node = head
        lth = 1
        while(head.next):
            head = head.next
            lth = lth+1
        tail_node = head
        #print(head_node,tail_node)
        tail_node.next = head_node
        #print(head_node)
        print(lth)
        for i in range(lth-k%lth-1):
            head_node = head_node.next
        tail_node = head_node.next
        head_node.next = None
        return tail_node
