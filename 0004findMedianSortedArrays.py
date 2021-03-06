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

    def findMedianSortedArrays1(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1_tmp = nums1
            nums2_tmp = nums2
            nums1 = nums2_tmp
            nums2 = nums1_tmp
            m = len(nums1)
            n = len(nums2)
        iMin,iMax = 0,m
        while(iMin<=iMax):
            i = (iMax+iMin)//2
            j = (m+n+1)//2-i
            if(j != 0 and i != m and nums2[j-1] > nums1[i]):
                iMin = i+1
            elif(i !=0 and j != n and nums1[i-1] > nums2[j]):
                iMax = i-1
            else:
                if i == 0:
                    maxLeft = nums2[j-1]
                elif j == 0:
                    maxLeft = nums1[i-1]
                else:
                    maxLeft = max(nums1[i-1],nums2[j-1])
                if (m+n)%2 != 0:
                    return maxLeft

                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i],nums2[j])


                return (maxLeft+minRight)/2.0

    def findKth(self,nums1,start1,end1,nums2,start2,end2,k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if (len1 > len2):
            return self.findKth(nums2,start2,end2,nums1,start1,end1,k)
        if len1 == 0:
            return nums2[start2 + k -1]
        if k == 1:
            return min(nums1[start1],nums2[start2])
        i = start1 + min(k//2,len1) - 1
        j = start2 + min(k//2,len2) - 1

        if nums1[i] >= nums2[j]:
            return self.findKth(nums1,start1,end1,nums2,j+1,end2,k - (j - start2 + 1))
        else:
            return self.findKth(nums1, i+1, end1, nums2, start2, end2, k - (i - start1 + 1))

    def findMedianSortedArrays2(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        return 0.5*(self.findKth(nums1,0,m-1,nums2,0,n-1,(m+n+1)//2)+self.findKth(nums1,0,m-1,nums2,0,n-1,(m+n+2)//2))




if __name__ == '__main__':
    sol = Solution()
    print(sol.findMedianSortedArrays2([1,2],[3,4]))