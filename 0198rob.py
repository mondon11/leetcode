#coding = utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lth = len(nums)
        if lth == 0:
            return 0
        if lth == 1:
            return nums[0]
        dp = [0] * (lth)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, lth):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([2,1,1,2,4]))