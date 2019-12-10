class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        ss = str(x)
        if len(ss) % 2 == 1:
            mid = len(ss) // 2
            for i in range(1,mid+1):
                if ss[mid-i] != ss[mid+i]:
                    return False
        else:
            left = len(ss) // 2 - 1
            right = len(ss) // 2
            while(left >= 0):
                if ss[left] != ss[right]:
                    return False
                left = left - 1
                right = right + 1
        return True

    def isPalindrome1(self,x):
        if x<0:
            return False
        div = 1
        while(x//div>=10):
            div = div * 10

        while(x != 0):
            right = x%10
            left = x//div
            if left != right:
                return False
            x = (x%div)//10
            div = div//100
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome1(1))