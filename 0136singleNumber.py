# coding = utf-8
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)==1:
            return nums[0]
        if nums[1]>nums[0]:
            return nums[0]
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return nums[len(nums)-1]
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]<nums[i+1]:
                return nums[i]
        return ""

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([2,2,1,1,1.5]))