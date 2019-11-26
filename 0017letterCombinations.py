# coding = utf-8
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dct = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        res = []

        if len(digits) == 0:
            return []
        self.backCombine('',digits,dct,res)
        return res

    def backCombine(self,combinations,next_digits,input,output):
        if len(next_digits) == 0:
            output.append(combinations)
        else:
            item = input[next_digits[0]]
            for i in item:
                self.backCombine(combinations+i,next_digits[1:],input,output)


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations('23'))