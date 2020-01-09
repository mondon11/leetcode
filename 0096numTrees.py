class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0] = 1
        for m in range(1,n+1):
            for i in range(0,m):
                dp[m] = dp[m] + dp[i]*dp[m-1-i]
        return dp[n]

