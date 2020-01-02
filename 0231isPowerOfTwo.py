class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while(1):
            if 2**i == n:
                return True
            if 2**i > n:
                return False
            i = i+1

    def isPowerOfTwo1(self, n):
        if n == 1:
            return True
        if n <= 0:
            return False
        while(n>1):
            m = n%2
            if m != 0:
                return False
            n = n//2
        return True

    def isPowerOfTwo2(self, n):
        return n>0 and n & (n-1) == 0