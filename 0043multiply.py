# coding = utf-8
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        l1 = len(num1)
        l2 = len(num2)
        res = '0'
        num2 = num2[::-1]
        num1 = num1[::-1]
        for i in range(l2):
            n2 = num2[i]
            carry = 0
            s = ''
            for j in range(l1):
                n1 = num1[j]
                tmp = int(n1) * int(n2) + carry
                carry = tmp // 10
                s = str(tmp % 10) + s
            s = str(carry) + s if carry else s
            for k in range(i):
                s = s + '0'
            res = self.addStrings(s,res)
        return res


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

if __name__ == '__main__':
    sol = Solution()
    print(sol.multiply('123','456'))