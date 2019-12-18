class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        row_num = len(matrix)
        col_num = len(matrix[0])
        used = [[False]*col_num for _ in range(row_num)]
        col_di = [1,0,-1,0]
        row_di = [0,1,0,-1]

        row_pos = 0
        col_pos = 0
        res = []
        step = 0
        for _ in range(row_num*col_num):
            used[row_pos][col_pos] = True
            res.append(matrix[row_pos][col_pos])

            row_next = row_pos + row_di[step]
            col_next = col_pos + col_di[step]

            if row_next >= 0 and row_next < row_num and col_next >=0 and col_next < col_num  and used[row_next][col_next] == False:
                row_pos = row_next
                col_pos = col_next
            else:
                step = (step + 1)%4
                row_pos = row_pos + row_di[step]
                col_pos = col_pos + col_di[step]
        return res




if __name__ == '__main__':
    sol = Solution()
    mt = [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]
    print(sol.spiralOrder(mt))