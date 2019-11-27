#coding = utf-8
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(id(nums))
        tmp = nums[:]
        nums.sort()
        combinations = []
        res = []
        self.recursivePermutation(combinations,nums,res)
        print(res)
        print(res.index(tmp))
        rs = res[res.index(tmp)+1] if res.index(tmp) < len(res)-1 else res[0]
        for i in range(len(nums)):
            nums[i] = rs[i]
        print(nums)
        print(id(nums))
    def recursivePermutation(self,combinations,next_nums,res):



        if len(next_nums) == 0:
            if combinations not in res:
                res.append(combinations)
                return
        for item in next_nums:
            cc = combinations + [item]
            nn = next_nums[:]
            nn.remove(item)
            self.recursivePermutation(cc,nn,res)

    def nextPermutation1(self, nums):
        lth = len(nums)
        i = lth - 2
        while(i >= 0):
            if nums[i]>=nums[i+1]:
                i = i-1
                continue
            else:
                index = self.findLarger(nums[i+1:],nums[i])
                tmp = nums[i+1+index]
                nums[i+1+index] = nums[i]
                nums[i] = tmp
                ll = nums[i+1:]
                ll.sort()
                nums[i+1:] = ll
                print(nums)
                return True
        nums.sort()
        print(nums)
        return True

    def findLarger(self,nums,target):
        dct = {}
        for index,item in enumerate(nums):
            if item>target and item not in dct.keys():
                dct[item] = index
        if len(dct) == 0:
            return -1
        min_num = min(dct.keys())
        min_index = dct[min_num]
        return min_index



if __name__ == '__main__':
    sol = Solution()
    print(sol.nextPermutation1([3,2,1]))
