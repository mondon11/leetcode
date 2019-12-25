# coding = utf-8
class Solution(object):
    def __init__(self):
        self.res = []
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)
        li = [int(i) for i in s]
        print(li)

        sum = 0
        for i in li:
            sum = sum+i**2
        if sum == 1:
            return True
        else:
            if sum in self.res:
                return False
            self.res.append(sum)
            return self.isHappy(sum)

    def isHappy1(self,n):
        def helper(n):
            s = str(n)
            li = [int(i) for i in s]
            #print(li)

            sum = 0
            for i in li:
                sum = sum + i ** 2
            return sum

        slow = n
        fast = n

        while(1):
            slow = helper(slow)
            fast = helper(fast)
            fast = helper(fast)
            if fast == 1:
                return True
            if slow == fast:
                return False