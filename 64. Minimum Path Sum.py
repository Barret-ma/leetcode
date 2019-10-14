# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        if height == 0: return 0
        width = len(grid[0])
        dirs = [(-1, 0), (0, -1)]
        dp = [[float('inf') for _ in range(width)] for _ in range(height)]
        dp[0][0] = grid[0][0]
        for i in range(height):
            for j in range(width):
                if i == 0 and j == 0:
                    continue
                for dir in dirs:
                    right = j + dir[0]
                    down = i + dir[1]
                    if right < 0 or down < 0 or right >= width or down >= height:
                        continue
                    dp[i][j] = min(dp[i][j], (dp[down][right] + grid[i][j]))
        return dp[height - 1][width - 1]

s = Solution()
s.minPathSum(
    [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
)


