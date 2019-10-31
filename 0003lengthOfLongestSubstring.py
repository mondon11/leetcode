# coding = utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        if n <= 1:
            return n
        for i in range(n):
            lookup = set()
            lookup.add(s[i])
            for j in range(i+1,n):
                if s[j] not in lookup:
                    lookup.add(s[j])
                else:
                    break
            max_len = max(len(lookup),max_len)
        return max_len

    def lengthOfLongestSubstring1(self, s):
        start = 0
        max_len = 0
        lookup = {}
        for cur in range(len(s)):
            # 重复出现的字母是不是在start-cur之间这个滑动窗口中，如果是则变start的位置
            if lookup.get(s[cur]) is not None: #重复出现
                if lookup[s[cur]] + 1 > start: #在滑动窗口之间
                    start = lookup[s[cur]] + 1
            lookup[s[cur]] = cur
            max_len = max(max_len, cur - start + 1)
        return max_len

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("pwwkep"))
    print(sol.lengthOfLongestSubstring1("pwwkep"))