# coding = utf-8
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        p1 = len(num1)-1
        p2 = len(num2)-1
        carry = 0
        res = ''
        while (p1 >= 0 and p2 >= 0):
            tmp = int(num1[p1]) + int(num2[p2]) + carry
            carry = tmp // 10
            res = str(tmp % 10)+res
            p1 = p1 - 1
            p2 = p2 - 1
        while (p1 >= 0):
            tmp = int(num1[p1]) + carry
            carry = tmp // 10
            res = str(tmp % 10)+res
            p1 = p1 - 1
        while (p2 >= 0):
            tmp = int(num2[p2]) + carry
            carry = tmp // 10
            res = str(tmp % 10)+res
            p2 = p2 - 1
        return res if not carry else '1' + res