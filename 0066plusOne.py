class Solution(object):
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = 0
        r = []
        for i in range(len(digits)):
            res = res + (10 ** (len(digits) - i - 1)) * digits[i]
        res = res + 1
        ss = str(res)
        for i in ss:
            r.append(int(i))
        return r

    def plusOne(self, digits):
        a = 0
        r = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                r = (digits[i] + 1) % 10
                a = (digits[i] + 1) // 10
                digits[i] = r
                if a == 0:
                    return digits

            else:
                r = (digits[i] + a) % 10
                a = (digits[i] + a) // 10
                digits[i] = r
                if a == 0:
                    return digits

            if i == 0 and a == 1:
                digits.insert(0, 1)

        print(digits)
        return digits

if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([4,3,9]))