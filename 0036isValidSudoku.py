# coding = utf-8
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = []
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            cols.append(col)

        areas = []
        i,j = 0,0
        while(i<=6):
            while(j<=6):
                areas.append([board[i][j],board[i+1][j],board[i+2][j],board[i][j+1],board[i+1][j+1],board[i+2][j+1],board[i][j+2],board[i+1][j+2],board[i+2][j+2]])
                j = j+3
            i = i+3
            j = 0

        boards = board+cols+areas

        for row in boards:
            for i in range(9):
                if row[i] == '.':
                    continue
                j = i+1
                while(j<=8):
                    if row[i] == row[j]:
                        return False
                    else:
                        j = j+1

        return True




    def isValidSudoku1(self, board):
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
                    return False
        return True



if __name__ == '__main__':
    board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

    sol = Solution()
    print(sol.isValidSudoku1(board))