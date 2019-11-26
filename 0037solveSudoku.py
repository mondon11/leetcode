# coding = utf-8
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        areas = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                areas_index = (i//3)*3+j//3
                if board[i][j] == '.':
                    continue
                if board[i][j] not in rows[i].keys() and board[i][j] not in cols[j].keys() and board[i][j] not in areas[areas_index].keys():
                    rows[i][board[i][j]] = 1
                    cols[j][board[i][j]] = 1
                    areas[areas_index][board[i][j]] = 1

                else:
                    print('No answer')
        print('Has answer')

        self.recursiveSolveSudoku(board,rows,cols,areas,0,0)


    def recursiveSolveSudoku(self,board, rows, cols, areas, row_num, col_num):

        if col_num == 9:
            col_num = 0
            row_num = row_num + 1
            if row_num == 9:
                return True

        if board[row_num][col_num] != '.':
            return self.recursiveSolveSudoku(board, rows, cols, areas, row_num, col_num + 1)
        else:
            for n in range(1, 10):
                areas_index = (row_num // 3) * 3 + col_num // 3
                if str(n) not in rows[row_num].keys() and str(n) not in cols[col_num].keys() and str(n) not in \
                        areas[areas_index].keys():
                    rows[row_num][str(n)] = 1
                    cols[col_num][str(n)] = 1
                    areas[areas_index][str(n)] = 1
                    board[row_num][col_num] = str(n)

                    if self.recursiveSolveSudoku(board, rows, cols, areas, row_num, col_num + 1):
                        return True

                    board[row_num][col_num] = '.'
                    rows[row_num].pop(str(n))
                    cols[col_num].pop(str(n))
                    areas[areas_index].pop(str(n))
        return False




if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(id(board))
    print(board)
    sol = Solution()
    sol.solveSudoku(board)
    print(id(board))
    print(board)
