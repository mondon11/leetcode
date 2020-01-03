# coding = utf-8
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        rt = [0]
        head = 1
        for i in range(n):
            for j in range(len(rt)-1,-1,-1):
                rt.append(rt[j]+head)
            head = head<<1
        return rt
