class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        res = [[0]*n for _ in range(n)]
        row_di = [0,1,0,-1]
        col_di = [1,0,-1,0]
        step = 0
        row_pos = 0
        col_pos = 0

        for i in range(1,n**2+1):
            res[row_pos][col_pos] = i
            row_next = row_pos + row_di[step]
            col_next = col_pos + col_di[step]
            if row_next>=0 and row_next<n and col_next>=0 and col_next<n and res[row_next][col_next] == 0:
                row_pos = row_next
                col_pos = col_next
            else:
                step = (step+1)%4
                row_pos = row_pos + row_di[step]
                col_pos = col_pos + col_di[step]
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(3))

