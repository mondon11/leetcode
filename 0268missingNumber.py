# coding = utf-8
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i,item in enumerate(nums):
            dic[item] = i
        for i in range(len(nums)+1):
            j = dic.get(i)
            if j == None:
                return i

    def missingNumber1(self, nums):
        n = len(nums)
        expectSum = (0+n)*(n+1)*0.5
        actualSum = 0
        for i in range(n):
            actualSum = actualSum + nums[i]
        return int(expectSum-actualSum)


if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber([0,1,2,3,5]))
