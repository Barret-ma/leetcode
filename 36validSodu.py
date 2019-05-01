class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            rows = set([])
            cols = set([])
            cube = set([])
            for j in range(len(board[i])):
                if (board[i][j] != '.' and board[i][j] in rows):
                    return False
                else:
                    rows.add(board[i][j])
                if (board[j][i] != '.' and board[j][i] in cols):
                    return False
                else:
                    cols.add(board[j][i])
                if (board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3] in cube and board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3] != '.'):
                    return False
                else:
                    cube.add(board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3])
        return True
                
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board1 = [
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

sodu = Solution()
# print sodu.isValidSudoku(board)
print sodu.isValidSudoku(board1)