
# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

# After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

# Example 1:

# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:

# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:

# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
 

# Notes:

# 1 <= grid.length = grid[0].length <= 50.
# 0 <= grid[i][j] <= 1.
from collections import defaultdict

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        color = 1
        areas = defaultdict(lambda: 0)
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    color += 1
                    areas[color] = self.getArea(grid, i, j, n, m, color)
                    ans = max(ans, areas[color])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    curArea = 1
                    colorSet = set([self.getColor(grid, i + 1, j, n, m), self.getColor(grid, i - 1, j, n, m), self.getColor(grid, i, j + 1, n, m), self.getColor(grid, i, j - 1, n, m)])
                    for c in colorSet:
                        curArea += areas[c]
                    ans = max(ans, curArea)
        return ans

    def getColor(self, grid, x, y, n, m):
        return 0 if x < 0 or y < 0 or x >= n or y >= m else grid[x][y]

    def getArea(self, grid, x, y, n, m, color):
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
            return 0
        grid[x][y] = color
        return 1 + self.getArea(grid, x + 1, y, n, m, color) + self.getArea(grid, x - 1, y, n, m, color) + self.getArea(grid, x, y + 1, n, m, color) + self.getArea(grid, x, y - 1, n, m, color)

# s = Solution()
# print(s.largestIsland([[1, 0], [0, 1]]))

s1 = Solution()
print(s1.largestIsland([[1, 1], [1, 0]]))