# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#   [2],
#   [3,4],
#   [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:

# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # version 1
        height = len(triangle)
        for i in range(height):
            for j in range(i + 1):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    triangle[i][0] += triangle[i - 1][0]
                elif j == i:
                    triangle[i][i] += triangle[i - 1][i - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
                
        return min(triangle[-1])

        # version 2  
        # height = len(triangle)
        # dp = [[float('inf') for i in range((len(triangle[_])))] for _ in range(height)]
        # dp[0][0] = triangle[0][0]
        # for i in range(height):
        #     for j in range(len(triangle[i])):
        #         if i == 0 and j == 0:
        #             continue
        #         if j < len(triangle[i - 1]):
        #             dp[i][j] = min(dp[i][j], triangle[i][j] + dp[i - 1][j])
        #         if j - 1 >= 0:
        #             dp[i][j] = min(dp[i][j], triangle[i][j] + dp[i - 1][j - 1])

        # return min(dp[height - 1])
    
s = Solution()
s.minimumTotal(
    [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
)