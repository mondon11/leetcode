# coding = utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return len(nums)
        i = 1
        j = 2
        while(j<len(nums)):
            if nums[j] == nums[i-1]:
                j = j+1
            else:
                i = i+1
                nums[i] = nums[j]
                j =j+1
        return i+1

if __name__ == '__main__':
    sol =Solution()
    print(sol.removeDuplicates([1,1,1]))
