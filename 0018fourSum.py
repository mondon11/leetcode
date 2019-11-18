# coding = utf-8
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        lth = len(nums)
        if lth < 4:
            return []
        res = []
        for i in range(lth):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,lth):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                start = j + 1
                end = lth - 1
                while(start < end):
                    tmp = nums[i] + nums[j] + nums[start] + nums[end]
                    if tmp == target:
                        res.append([nums[i],nums[j],nums[start],nums[end]])
                        while(start < end and nums[start] == nums[start+1]):
                            start = start + 1
                        while (start < end and nums[end] == nums[end - 1]):
                            end = end - 1
                        start = start + 1
                        end = end -1
                    elif tmp > target:
                        end = end - 1
                    else:
                        start = start + 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum([1, 0, -1, 0, -2, 2],0))

