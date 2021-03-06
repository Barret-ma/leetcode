# There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

 

# Example 1:

# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:

# Example 2:

# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:

 

# Note:

# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[0 for x in range(n)] for _ in range(m)]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dp[i][j] = 1
        totalOut = 0
        for q in range(N):
            dp1 = [[0 for w in range(n)] for _ in range(m)]
            for l in range(m):
                for j in range(n):
                    for dir in dirs:
                        x = j + dir[0]
                        y = l + dir[1]
                        if (x < 0 or x >= n or y < 0 or y >= m):
                            if dp[l][j] >= 1:
                                totalOut += 1
                            continue
                        dp1[l][j] += dp[y][x]
            dp = dp1
        print(totalOut)
        return totalOut % 1000000007
                        
s = Solution()
s.findPaths(2, 2, 2, 0, 0)
s.findPaths(1, 3, 3, 0, 1)