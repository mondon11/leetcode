# coding = utf-8
import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        li = re.findall('^[\+\-]?\d+', str.lstrip())
        if not li:
            return 0
        return max(min(int(li[0]),((1<<31)-1)),-(1<<31))

if __name__ == '__main__':
    sol = Solution()
    print(sol.myAtoi('7-1234ll'))