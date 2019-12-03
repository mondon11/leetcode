#coding = utf-8
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        combinations = []
        start = 0
        end = len(nums)
        self.helper(start,end,combinations,nums,res)
        print(res)
        return res



    def helper(self,start,end,combinations,nums,res):
        res.append(combinations)
        print(combinations)
        for i in range(start,end):
            self.helper(i+1,end,combinations+[nums[i]],nums,res)
            #print(res)


if __name__ == '__main__':
    sol = Solution()
    sol.subsets([1,2,3,4])