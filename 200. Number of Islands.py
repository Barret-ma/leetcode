# Given a 2d grid map of '1's (land) and '0's (water), 
# count the number of islands. An island is surrounded 
# by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four 
# edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not len(grid[0]):
            return 0

        length = len(grid)
        height = len(grid[0])
        result = 0
        for j in range(length):
            for i in range(height):
                if grid[j][i] == '1':
                    result += 1
                    self.dfs(grid, i, j, length, height)
        return result
    def dfs(self, grid, x, y, m, n):
        if x < 0 or y < 0 or x >= n or y >= m or grid[y][x] == '0':
            return
        grid[y][x] = '0'
        self.dfs(grid, x + 1, y, m, n)
        self.dfs(grid, x - 1, y, m, n)
        self.dfs(grid, x, y + 1, m, n)
        self.dfs(grid, x, y - 1, m, n)