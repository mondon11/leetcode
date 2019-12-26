class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        forward = [nums[0]]
        backward = [nums[-1]]
        for i in range(1,len(nums)):
            forward.append(forward[i-1]*nums[i])
            backward.append(backward[i-1]*nums[len(nums)-i-1])
        backward.reverse()
        print(forward)
        print(backward)
        res = [backward[1]]
        for i in range(1,len(nums)-1):
            res.append(forward[i-1]*backward[i+1])
        res.append(forward[-2])
        return res

    def productExceptSelf1(self, nums):
        tmp = 1
        res = []
        for i in range(len(nums)):
            res.append(tmp)
            tmp = tmp * nums[i]
        tmp = 1

        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*tmp
            tmp = tmp * nums[i]
        return res

