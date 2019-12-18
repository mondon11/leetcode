class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        lth = len(nums)
        mid = lth // 2
        return nums[mid]

if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([1,3,3,4,3]))