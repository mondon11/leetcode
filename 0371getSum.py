# coding = utf-8
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a,b])

if __name__ == '__main__':
    sol = Solution()
    res = sol.getSum(-1,2)
    print(res)