class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        res = nums[0]
        for i in range(len(nums)):
            if sum > 0:
                sum = sum+nums[i]
            else:
                sum = nums[i]
            res = max(res,sum)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))