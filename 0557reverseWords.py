class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverseWord(w):
            w = [i for i in w]
            i = 0
            j = len(w)-1
            while(i<j):
                tmp = w[i]
                w[i] = w[j]
                w[j] = tmp
                i = i+1
                j = j-1
            return ''.join(w)
        res = ''
        for word in s.split(' '):
            #print(word)
            tmp = reverseWord(word)
            res = res + ' ' +tmp
        return res.strip()

    def reverseWords1(self,s):
        return ' ' .join([w[::-1] for w in s.split(' ')])

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords1('Let\'s take LeetCode contest'))