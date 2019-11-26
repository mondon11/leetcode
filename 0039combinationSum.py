#coding = utf-8
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        combinations = []
        res = []
        self.recursiveCombination(combinations,candidates,res,target)

        print(res)
        print(len(res))

        return res


    def recursiveCombination(self,combinations,candidates,res,target):
        #if len(combinations) >= target//candidates[0]:
            #res.append(combinations)
        #    return True
        for item in candidates:
            ss = combinations + [item]
            ss.sort()
            if ss not in res and sum(ss) == target:
                res.append(ss)
                return True
            if sum(ss)>= target:
                return True
            else:
                self.recursiveCombination(ss,candidates,res,target)

    def combinationSum1(self,candidates,target):
        print(1)

    def recursiveCombination1(self,combinations,candidates,res,target):
        print(2)


if __name__ == '__main__':
    sol = Solution()

    print(sol.combinationSum([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73],310))
