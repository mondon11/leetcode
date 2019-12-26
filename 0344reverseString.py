class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        mid = len(s)//2
        for i in range(mid):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp

    def reverseString1(self, s):
        i = 0
        j = len(s)-1
        while(i < j):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i = i+1
            j = j-1
