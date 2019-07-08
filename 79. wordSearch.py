class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not len(board) or not len(board[0]):
            return False
        m = len(board)
        n = len(board[0])
        self.ly = m
        self.lx = n
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.search(board, word, 0, i, j, visited):
                    return True
        return False
                
    def search(self, board, word, index, i, j, visited):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= self.ly or j >= self.lx or visited[i][j] or board[i][j] != word[index]:
            return False

        visited[i][j] = True
        res = self.search(board, word, index + 1, i + 1, j, visited) or self.search(board, word, index + 1, i, j + 1, visited) or \
                    self.search(board, word, index + 1, i - 1, j, visited) or \
                        self.search(board, word, index + 1, i, j - 1, visited)
        visited[i][j] = False
        return res

s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print s.exist(board, 'ABCCED')
print s.exist(board, 'SEE')
print s.exist(board, 'ABCB')