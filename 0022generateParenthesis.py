#coding = utf-8
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        combinations = ['0' for i in range(2*n)]
        next_chose = []
        for i in range(2*n):
            next_chose = next_chose + [i]
        self.helper(combinations,next_chose,res)
        res = set(res)
        print(res)
        return res


    def helper(self,combinations,next_chose,res):
        #if len(next_chose) == 0 and ''.join(combinations[:]) not in res:
        if len(next_chose) == 0:
            res.append(''.join(combinations[:]))
            #print(combinations)
            return
        for i in next_chose:
            for j in next_chose:
                if j > i:
                    combinations[i] = '('
                    combinations[j] = ')'
                    next_chose.remove(i)
                    next_chose.remove(j)

                    self.helper(combinations,next_chose,res)
                    combinations[i] = '0'
                    combinations[j] = '0'
                    next_chose.append(i)
                    next_chose.append(j)




    def generateParenthesis1(self, n):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans



if __name__ == '__main__':
    sol = Solution()
    sol.generateParenthesis(2)

