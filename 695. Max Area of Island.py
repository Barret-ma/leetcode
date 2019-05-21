# Given a non-empty 2D array grid of 0's and 1's, an island is a 
# group of 1's (representing land) connected 4-directionally 
# (horizontal or vertical.) You may assume all four edges of the 
# grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. 
# (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because 
# the island must be connected 4-directionally.
# Example 2:

# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        mx = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    mx = max(self.dfs(grid, i, j, n, m), mx)
        return mx
        
    def dfs(self, grid, x, y, n, m):
        if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        return (1 + self.dfs(grid, x + 1, y, n, m) + self.dfs(grid, x - 1, y, n, m) 
                    + self.dfs(grid, x, y + 1, n, m) + self.dfs(grid, x, y - 1, n, m))

s = Solution()
print(s.maxAreaOfIsland(
    [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
))

s1 = Solution()
print(s1.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))