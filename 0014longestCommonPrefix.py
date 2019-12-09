class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        res = strs[0]
        for i in range(1,len(strs)):
            res = self.findCommonStr(res,strs[i])
        return res

    def findCommonStr(self,str1,str2):
        n = min(len(str1),len(str2))
        res = ''
        for i in range(n):
            if str1[i] == str2[i]:
                res = res+str1[i]
            else:
                break
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["dog","racecar","car"]))