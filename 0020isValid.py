#coding = utf-8
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li = []
        for i in range(len(s)):
            li.append(s[i])
            if len(li)>1:
                if (li[-1] == ')' and li[-2] == '(') or (li[-1] == ']' and li[-2] == '[') or (li[-1] == '}' and li[-2] == '{'):
                    li.pop()
                    li.pop()


        if len(li) > 0:
            return False
        else:
            return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("()"))