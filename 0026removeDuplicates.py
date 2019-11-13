# coding = utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while(j<len(nums)):
            if nums[i] != nums[j]:
                i = i+1
                nums[i] = nums[j]
                j = j+1
            else:
                j = j+1
        return i+1


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1,1,2,2,2,3]))