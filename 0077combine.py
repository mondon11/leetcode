class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combinations = []
        next_chose = [i for i in range(1,n+1)]
        res = []
        self.helper(combinations,next_chose,res,k)
        print(res)
        return res

    def helper(self,combinations,next_chose,res,k):
        if len(combinations) == k:
            res.append(combinations[:])
            return
        for i in range(len(next_chose)):
            if len(combinations) == 0:
                combinations = combinations + [next_chose[i]]
                nn_ = next_chose[:]
                for j in range(i,-1,-1):
                    next_chose.pop(j)
                self.helper(combinations, next_chose, res, k)
                combinations.pop()
                next_chose = nn_[:]

            elif combinations[-1] < next_chose[i]:
                # combinations = combinations + [next_chose[i]]
                # nn = next_chose.pop(i)
                # self.helper(combinations,next_chose,res,k)
                # combinations.pop()
                # next_chose.insert(i,nn)
                combinations = combinations + [next_chose[i]]
                nn_ = next_chose[:]
                for j in range(i, -1, -1):
                    next_chose.pop(j)
                self.helper(combinations, next_chose, res, k)
                combinations.pop()
                next_chose = nn_[:]

    def combine1(self,n,k):
        combinations = []
        index = 1
        res = []
        self.helper1(combinations,index,res,n,k)
        print(res)
        return res

    def helper1(self,combinations,index,res,n,k):
        if len(combinations) == k:
            res.append(combinations[:])
            return
        for i in range(index,n+1):
            combinations.append(i)
            self.helper1(combinations,i+1,res,n,k)
            combinations.pop()

if __name__ == '__main__':
    sol = Solution()
    sol.combine1(4,3)