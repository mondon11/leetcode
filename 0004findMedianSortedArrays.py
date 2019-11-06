#coding = utf-8
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        li = []
        i = 0
        j = 0
        while(i<len1 and j<len2):
            if nums1[i] < nums2[j]:
                li.append(nums1[i])
                i = i+1
            else:
                li.append(nums2[j])
                j = j+1
        while(i<len1):
            li.append(nums1[i])
            i = i+1
        while(j<len2):
            li.append(nums2[j])
            j = j+1

        if len(li)%2 != 0:
            return li[len(li)//2]
        else:
            return 0.5*(li[len(li)//2-1]+li[len(li)//2])

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays([1,2],[3,4]))