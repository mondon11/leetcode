# coding = utf-8
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        numCols = len(s)
        li = [[0 for i in range(numCols)] for j in range(numRows)]
        i = 0
        j = 0
        flag = 1
        for c in range(numCols):
            if (i<numRows and flag):
                li[i][j] = s[c]
                i = i+1
                if i == numRows:
                    i = i-1
                    flag = 0
                continue
            #flag = 0
            #i = i-1
            if (i>0):
                j = j+1
                i = i-1
                li[i][j] = s[c]
                if i == 0:
                    i = i+1
                    flag = 1
                continue
            #i = i+1
            #flag = 1
        res = ''
        for row in range(numRows):
            for col in range(numCols):
                if li[row][col] != 0:
                    res = res + li[row][col]
        return res

    def convert1(self, s, numRows):
        if numRows<2:
            return s
        li = ['' for _ in range(numRows)]
        i = 0
        flag = -1
        for c in s:
            li[i] = li[i]+c
            if i == 0 or i == numRows-1:
                flag = -flag
            i = i+flag
        return ''.join(li)

if __name__ == '__main__':
    sol = Solution()
    res = sol.convert1('abcdef',3)
    print(res)