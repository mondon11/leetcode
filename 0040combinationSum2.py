#coding = utf-8
class Solution(object):
    def combinationSum2(self, candidates, target):
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


    def recursiveCombination(self,combinations,next_candidates,res,target):
        #if len(combinations) >= target//candidates[0]:
            #res.append(combinations)
        #    return True
        for item in next_candidates:
            ss = combinations + [item]
            ss.sort()
            if ss not in res and sum(ss) == target:
                res.append(ss)
                return True
            if sum(ss)>= target:
                return True
            else:
                #ll = next_candidates.copy() #python3
                ll = next_candidates[:] #python2
                ll.remove(item)
                self.recursiveCombination(ss,ll,res,target)




if __name__ == '__main__':
    sol = Solution()

    print(sol.combinationSum2([10,1,2,7,6,1,5],8))
