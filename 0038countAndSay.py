# coding = utf-8
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n==1:
            return '1'
        else:
            return self.recursiveDivide('1',1,n)

    def recursiveDivide(self,combinations,count,target):
        if count >= target:
            return combinations
        else:

            i = 1
            ss = ''
            cc = 1

            if len(combinations) == 1:
                ss = '11'
            while(i<len(combinations)):

                if combinations[i] == combinations[i-1]:
                    i = i+1
                    cc = cc+1
                    if i == len(combinations):
                        ss = ss + str(cc) + combinations[i - 1]
                else:
                    ss=ss+str(cc)+combinations[i-1]
                    i = i+1
                    cc = 1
                    if i == len(combinations):
                        ss = ss + str(cc) + combinations[i - 1]


            return self.recursiveDivide(ss,count+1,target)

if __name__ == '__main__':
    sol = Solution()
    print(sol.countAndSay(6))