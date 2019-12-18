# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstnode = ListNode(0)
        lastnode = firstnode
        while(l1 != None and l2 != None):
            if l1.val <= l2.val:
                lastnode.next = l1
                lastnode = lastnode.next
                l1 = l1.next
            else:
                lastnode.next = l2
                lastnode = lastnode.next
                l2 = l2.next
        if l1 != None:
            lastnode.next = l1
        if l2 != None:
            lastnode.next = l2

        return firstnode.next

def generateList(l):
    prenode = ListNode(0)
    lastnode = prenode
    for item in l:
        lastnode.next = ListNode(item)
        lastnode = lastnode.next
    return prenode.next

if __name__ == '__main__':
    sol = Solution()
    l1 = generateList([1,2,4])
    l2 = generateList([1,3,4])
    print(sol.mergeTwoLists(l1,l2))
