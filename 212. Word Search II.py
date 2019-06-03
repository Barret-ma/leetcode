# Given a 2D board and a list of words from the dictionary, 
# find all words in the board.

# Each word must be constructed from letters of sequentially 
# adjacent cell, where "adjacent" cells are those horizontally 
# or vertically neighboring. The same letter cell may not be 
# used more than once in a word.

 

# Example:

# Input: 
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]

# Output: ["eat","oath"]
 

# Note:

# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
from collections import defaultdict

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return
        if not words:
            return
        m = len(board)
        n = len(board[0])

        wordMap = defaultdict(lambda: 0)
        results = set()
        for word in words:
            wordMap[word] = 1
            # wordMap[word[::-1]] = 1
        
        for i in range(m):
            for j in range(n):
                result = self.dfs(board, '', i, j, wordMap)
                if result:
                    results.add(result)
        return list(results)

    def dfs(self, grid, str, x, y, wordMap):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
            return False
        
        temp = grid[x][y]
        str += grid[x][y]
        if str in wordMap:
            return str
        isIn = False
        for (key, value) in wordMap.items():
            if str == key[:len(str)]:
                isIn = True
                break
        if not isIn:
            return False

        grid[x][y] = 0
        x1 = self.dfs(grid, str, x + 1, y, wordMap)
        x2 = self.dfs(grid, str, x - 1, y, wordMap)
        x3 = self.dfs(grid, str, x, y + 1, wordMap)
        x4 = self.dfs(grid, str, x, y - 1, wordMap)
        # if not r:
        grid[x][y] = temp
        if x1 or x2 or x3 or x4:
            return x1 or x2 or x3 or x4
        
        # else:
        #     return r

s = Solution()
print(s.findWords([
    ['o','a','o','n'],
    ['e','t','a','e'],
    ['i','h','e','r'],
    ['i','f','l','v']
], ["oath","pea","eat","rain"]))
