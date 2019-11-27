#coding = utf-8
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lth = len(needle)
        if lth > len(haystack):
            return -1
        if lth == 0:
            return 0
        i = 0
        while(i <= len(haystack)-lth):
            ss = haystack[i:i+lth]
            if ss == needle:
                return i
            i = i+1
        return -1

    def strStr1(self,haystack,needle):
        lth = len(needle)
        if lth > len(haystack):
            return -1
        if lth == 0:
            return 0
        dct = self.calDct(needle)
        i = 0
        while(i <= len(haystack)-lth):
            ss = haystack[i:i+lth]
            if ss == needle:
                return i
            elif i == len(haystack)-lth:
                return -1
            elif haystack[i+lth] not in dct.keys():
                i = i+lth+1
            else:
                i = i+dct[haystack[i+lth]]
        return -1

    def calDct(self,needle):
        lth = len(needle)
        dct = {}
        i = lth - 1
        while(i>=0):
            if needle[i] not in dct.keys():
                dct[needle[i]] = lth - i
            i = i-1
        return dct

if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr1('aaaaa','bba'))
