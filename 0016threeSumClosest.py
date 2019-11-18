# coding = utf-8
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lth = len(nums)
        if lth < 3:
            return 0
        res = nums[0] + nums[1] +nums[2]
        for i in range(lth):
            for j in range(i+1,lth):
                for k in range(j+1,lth):
                    if abs(nums[i] + nums[j] + nums[k] - target) <= abs(res - target):
                        res = nums[i] + nums[j] + nums[k]
        return res

    def threeSumClosest1(self,nums,target):
        nums.sort()
        lth = len(nums)
        if lth < 3:
            return 0
        res = nums[0] + nums[1] +nums[2]
        for i in range(lth):
            start = i + 1
            end = lth - 1
            while(start<end):
                tmp = nums[i] + nums[start] + nums[end]
                if tmp == target:
                    return tmp
                if abs(tmp - target) <= abs(res - target):
                    res = tmp
                if tmp < target:
                    start = start + 1
                else:
                    end = end - 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSumClosest1([-1,2,1,-4],1))