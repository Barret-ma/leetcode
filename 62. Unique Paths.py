# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Above is a 7 x 3 grid. How many possible unique paths are there?

# Note: m and n will be at most 100.

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:

# Input: m = 7, n = 3
# Output: 28


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dirs = [(-1, 0), (0, -1)]
        dp = [[0 for i in range(m)] for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                for dir in dirs:
                    right = j + dir[0]
                    down = i + dir[1]
                    if right < 0 or down < 0 or right >= m or down >= n:
                        continue
                    dp[i][j] += dp[down][right]
        return dp[n - 1][m - 1]

s = Solution()
print(s.uniquePaths(7, 3))