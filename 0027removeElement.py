# coding = utf-8
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        while(i<len(nums)):
            if nums[i] == val:
                nums.remove(val)
                i = i-1
            i = i+1
        return len(nums)

    def removeElement1(self, nums, val):
        i = 0
        j = 0
        while(j<len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i+1
                j = j+1
            else:
                j = j+1
        return i




if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement1([1,2,3,4,2],2))