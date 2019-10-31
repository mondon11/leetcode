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
            if lookup.get(s[cur]) is None:
                lookup[s[cur]] = cur
                max_len = max(max_len,cur- start +1)
            else:
                start = max(lookup[s[cur]]+1,start)
                lookup[s[cur]] = cur
                max_len = max(max_len, cur - start + 1)
        return max_len

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("pwwkep"))
    print(sol.lengthOfLongestSubstring1("pwwkep"))