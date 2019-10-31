# coding = utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return n
        start = 0
        max_len = 0
        hashtable = {}
        for cur in range(n):
            item = hashtable.get(s[cur])
            if item is None:
                hashtable[s[cur]] = cur
            else:
                max_len_in = cur - start
                start = hashtable[s[cur]] + 1
                hashtable[s[cur]] = cur
                if max_len_in > max_len:
                    max_len = max_len_in
        return max_len