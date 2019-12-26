class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(n):
            if n == 0:
                return False
            if n == 1 or n == 2 or n == 3:
                return True
            return  not (helper(n-1) and helper(n-2) and helper(n-3))

        return helper(n)

    def canWinNim1(self,n):
        return n%4

if __name__ == '__main__':
    sol = Solution()
    print(sol.canWinNim(34))