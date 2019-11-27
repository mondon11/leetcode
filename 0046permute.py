# coding = utf-8
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        combinations = []
        self.recursivePermute(combinations,nums,res)
        print(res)
        return res

    def recursivePermute(self,combinations,next_nums,res):
        if len(next_nums) == 0:
            res.append(combinations)
            return
        for i in range(len(next_nums)):
            cc = combinations+[next_nums[i]]
            nn = next_nums[:i]+next_nums[i+1:] if i < len(next_nums)-1 else next_nums[:i]
            self.recursivePermute(cc,nn,res)

if __name__ == '__main__':
    sol = Solution()
    sol.permute([1,2,1])