class Solution(object):
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1:
            return n
        if n == 1:
            return m
        path = []
        used = {'down':False,'right':False}
        down_count = 1
        right_count = 1
        res = []
        self.helper(path,used,res,m,n,down_count,right_count)
        return len(res)

    def helper(self,path,used,res,m,n,down_count,right_count):
        if used['down'] == True and used['right'] == True:
            res.append(path[:])
            return
        for i in ['down','right']:
            if not used[i]:
                path.append(i)
                if i == 'down':
                    down_count = down_count + 1
                else:
                    right_count = right_count + 1

                if down_count == n:
                    used['down'] = True
                if right_count == m:
                    used['right'] = True
                self.helper(path,used,res,m,n,down_count,right_count)
                path.pop()

                if i == 'down':
                    if down_count == n:
                        used['down'] = False
                    down_count = down_count - 1
                else:
                    if right_count == m:
                        used['right'] = False
                    right_count = right_count - 1

    def uniquePaths(self, m, n):
        dp = [[ 1 for i in range(m)] for j in range(n)]
        print(dp)
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePaths(3,2))



