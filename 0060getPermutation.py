class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        combinations = []
        next_chose = [str(i) for i in range(1,n+1)]
        res =[]
        used = [False for _ in range(n)]
        #self.helper(combinations,next_chose,res,n,k)
        self.helper1(combinations, next_chose,used, res, n, k,0)
        ss = ''.join(res[-1])
        print(ss)
        return ss

    def helper(self,combinations,next_chose,res,n,k):
        if len(combinations) == n:
            res.append(combinations[:])
            return
        if len(res) == k:
            return
        for i in range(len(next_chose)):
            combinations.append(next_chose[i])
            nn = next_chose.pop(i)
            self.helper(combinations,next_chose,res,n,k)
            combinations.pop()
            next_chose.insert(i,nn)

    def helper1(self,combinations,next_chose,used,res,n,k,depth):
        if depth == n:
            res.append(combinations[:])
            print(res)
            return
        nums = self.factorial(n-1-depth)
        for i in range(n):
            if used[i]:
                continue
            if nums < k:
                k = k-nums
                continue
            combinations.append(next_chose[i])
            used[i] = True
            self.helper1(combinations, next_chose, used,res, n, k,depth+1)




    def factorial(self,n):
        res = 1
        while(n):
            res = n*res
            n = n-1
        return res

if __name__ == '__main__':
    sol = Solution()
    sol.getPermutation(4,3)