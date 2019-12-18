class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_bak = nums1[:m]
        nums1[:] = []

        i = 0
        j = 0

        while(i<m and j<n):
            if nums1_bak[i] > nums2[j]:
                nums1.append(nums2[j])
                j = j+1
            else:
                nums1.append(nums1_bak[i])
                i = i+1
        if i < m:
            nums1[i+j:] = nums1_bak[i:]
        if j < n:
            nums1[i + j:] = nums2[j:]
        print(nums1)

if __name__ == '__main__':
    sol = Solution()
    sol.merge([1,2,3,0,0,0],3,[3,6,7],3)