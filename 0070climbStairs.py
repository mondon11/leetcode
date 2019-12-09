class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        combinations = []
        next_chose = [1,2]
        res = []
        self.helper(combinations,next_chose,res,n)
        print(res)
        return len(res)


    def helper(self,combinations,next_chose,res,n):
        if sum(combinations) == n:
            res.append(combinations[:])
            return
        for i in next_chose:
            if sum(combinations) < n:
                combinations = combinations + [i]
                self.helper(combinations,next_chose,res,n)
                combinations.pop()

    def climbStairs1(self,n):
        res = []
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        res.append(0)
        res.append(1)
        res.append(2)
        for i in range(3,n+1):
            res.append(res[i-1] + res[i-2])
        r = res.pop()
        print(r)
        return r

if __name__ == '__main__':
    sol = Solution()
    sol.climbStairs1(5)