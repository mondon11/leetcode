# coding = utf-8
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_l = []
        le = len(nums)
        nums.sort()
        if le < 3:
            return res_l
        for i in range(0,le-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = le-1
            while(j < k):
                if nums[i]+nums[j]+nums[k] == 0:
                    res_l.append([nums[i],nums[j],nums[k]])
                    j = j + 1
                    k = k - 1
                    while j<k and (nums[j] == nums[j - 1]):
                        j = j + 1
                    while j<k and (nums[k] == nums[k + 1]):
                        k = k - 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j = j + 1
                    while j<k and (nums[j] == nums[j - 1]):
                        j = j + 1
                else:
                    k = k - 1
                    while j<k and (nums[k] == nums[k + 1]):
                        k = k - 1
        return res_l

if __name__ == '__main__':
    sol = Solution()
    res = sol.threeSum([-2,0,1,1,1,1,2])
    print(res)