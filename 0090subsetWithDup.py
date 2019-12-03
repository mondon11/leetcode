#coding = utf-8
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        combinations = []
        start = 0
        end = len(nums)
        nums.sort()
        self.helper(start,end,combinations,nums,res)
        print(res)
        return res



    def helper(self,start,end,combinations,nums,res):
        res.append(combinations)
        print(combinations)
        for i in range(start,end):
            if i>start and nums[i] == nums[i-1]:
                continue
            self.helper(i+1,end,combinations+[nums[i]],nums,res)
            #print(res)


if __name__ == '__main__':
    sol = Solution()
    sol.subsetsWithDup([1,2,2])