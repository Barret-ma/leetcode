class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return [["Q"]]
        space = [['.'] * n for _ in range(n)]
        result = []

        def isAttachEachOther(board, x, y):
            # x1 = 0
            y1 = 0

            x2 = x
            y2 = y
            
            while y1 < x:
                
                if board[y1][y][0] != '.':
                    return True
                y1 += 1

            while x2 >= 0 and y2 >= 0:
                if board[x2][y2][0] != '.':
                    return True
                x2 -= 1
                y2 -= 1
                
            while x >= 0 and y < len(board):
                
                if board[x][y][0] != '.':
                    return True
                x -= 1
                y += 1
            return False

        def findDistinctPath(board, index):
            if index > n - 1:
                strBoard = []
                for i in range(len(board)):
                    strBoard.append(''.join(board[i]))
                result.append(strBoard)
                return
            # if index == n - 1:
                
            for i in range(n):
                if isAttachEachOther(board, index, i):
                    continue
                board[index][i] = 'Q'
                findDistinctPath(board, index + 1)
                board[index][i] = '.'
                
        findDistinctPath(space, 0)
        return result

s = Solution()
print s.solveNQueens(5)
        