# coding = utf-8
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lth = len(nums)
        if lth ==0:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[lth-1]:
            return lth
        if target == nums[lth-1]:
            return lth-1
        for i in range(lth):
            if target > nums[i]:
                continue
            else:
                return i

    def searchInsert1(self, nums, target):
        lth = len(nums)
        start = 0
        end = lth - 1
        while(start <= end):
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert1([1,3,5,6],0))