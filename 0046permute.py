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

    def permute1(self, nums):
        if len(nums) == 0:
            return []
        used = [False] * len(nums)
        res = []
        self.__dfs(nums, 0, [], used, res)
        return res

    def __dfs(self, nums, index, pre, used, res):
        if index == len(nums):
            res.append(pre.copy())
            print(pre)
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                pre.append(nums[i])
                self.__dfs(nums, index + 1, pre, used, res)
                used[i] = False
                pre.pop()



if __name__ == '__main__':
    sol = Solution()
    sol.permute1([1,2,3])