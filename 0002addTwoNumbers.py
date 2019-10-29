# coding = utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        cur = res
        c = 0
        while(l1 != None and l2 != None):
            p = l1.val
            q = l2.val
            s = (p + q + c)%10
            c = (p + q + c)//10
            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while(l1 != None and l2 == None):
            p = l1.val
            s = (p + c)%10
            c = (p + c)//10
            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next
        while (l1 == None and l2 != None):
            q = l2.val
            s = (q + c) % 10
            c = (q + c) // 10
            cur.next = ListNode(s)
            cur = cur.next
            l2 = l2.next
        while (l1 == None and l2 == None):
            s = c
            if c == 0:
                break
            else:
                cur.next = ListNode(s)
                cur = cur.next
                break

        return res.next

    def addTwoNumbers1(self, l1, l2):
        res = ListNode(0)
        cur = res
        c = 0
        while (c or l1 or l2):
            s = (c + (l1.val if l1 else 0) + (l2.val if l2 else 0))%10
            c = (c + (l1.val if l1 else 0) + (l2.val if l2 else 0))//10
            cur.next = ListNode(s)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next


def generateList(l):
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

if __name__ == '__main__':
    l1 = generateList([2,4,3])
    l2 = generateList([5,6,4,8])
    sol = Solution()
    res = sol.addTwoNumbers1(l1,l2)
    print(1)