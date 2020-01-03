# coding = utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rt = 0
        tmp = abs(x)
        while(tmp):
            pop = tmp % 10
            tmp = tmp // 10
            rt = rt * 10 + pop
        res =  rt if x > 0 else -1*rt
        if res > ((1<<31) - 1) or res < -1*(1<<31):
            return 0
        else:
            return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(-123))