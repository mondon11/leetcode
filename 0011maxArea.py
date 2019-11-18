# coding = utf-8
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lth = len(height)
        if lth < 2:
            return 0
        maxArea = 0
        for i in range(lth):
            for j in range(i+1,lth):
                area = min(height[i],height[j]) * (j-i)
                maxArea = max(area,maxArea)
        return maxArea

    def maxArea1(self,height):
        i = 0
        j = len(height)-1
        maxArea = 0
        if j < 1:
            return 0
        while(i<j):
            maxArea = max(min(height[i], height[j]) * (j - i),maxArea)
            if height[i] > height[j]:
                j = j-1
            else:
                i = i+1
        return maxArea

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea1([1,8,6,2,5,4,8,3,7]))
