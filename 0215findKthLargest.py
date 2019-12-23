class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        self.quickSort(nums,0,len(nums)-1)
        return nums[len(nums)-k]

    def partition(self,nums,left,right):
        l = left
        r = right

        tmp = nums[l]
        nums[l] = nums[(l+r)//2]
        nums[(l + r) // 2] = tmp

        tmp = nums[l]
        while(l < r):
            while(l < r and nums[r] > tmp):
                r = r -1
            if l < r:
                nums[l] = nums[r]
                l = l + 1
            while(l < r and nums[l] <= tmp):
                l = l + 1
            if l < r:
                nums[r] = nums[l]
                r = r - 1
        nums[l] = tmp

        return l

    def quickSort(self,nums,left,right):
        if left < right:
            n = self.partition(nums,left,right)
            self.quickSort(nums,left,n-1)
            self.quickSort(nums,n+1,right)



if __name__ == '__main__':
    sol = Solution()
    li = [3, 2, 1, 5, 6, 4]
    print(sol.findKthLargest(li,2))


