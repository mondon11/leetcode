# coding = utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        le = len(nums)
        for i in range(0,le):
            for j in range(i+1,le):
                if nums[i]+nums[j] == target:
                    return [i,j]

    def twoSum1(self, nums, target):
        dct = {}
        for i,n in enumerate(nums):
            dct[n] = i
        for i,n in enumerate(nums):
            j = dct.get(target-n)
            if j is not None and j != i:
                return [i,j]

    def twoSum2(self, nums, target):
        dct = {}
        for i,n in enumerate(nums):
            j = dct.get(target - n)
            if j is not None:
                return [i,j]
            dct[n] = i

if __name__ == '__main__':
    sol = Solution()
    res = sol.twoSum([2,2,7,11,15],13)
    res1 = sol.twoSum1([2,2,7,11,15],13)
    res2 = sol.twoSum2([2,2,7,11,15],13)
    print(res,res1,res2)