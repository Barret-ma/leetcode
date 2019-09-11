# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example:

# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        
        res = 0
        for i in range(m):
            heights = self.buildRectangles(matrix, i)
            res = max(res, self.largetsRectangles(heights))
        print(res)
        return res
    def largetsRectangles(self, heights):
        res = 0
        stack = []
        heights.append(0)
        l = len(heights)
        i = 0
        while i < l:
            if len(stack) == 0 or heights[stack[-1]] < heights[i]:
                stack.append(i)
            else:
                cur = stack.pop()
                res = max(res, heights[cur] * (i if len(stack) == 0 else (i - stack[-1] - 1)))
                i -= 1
            i += 1
        return res
    def buildRectangles(self, grid, bottom):
        heights = []
        n = len(grid[0])
        
        for i in range(n):
            j = bottom
            height = 0
            while j >= 0:
                if grid[j][i] == '0':
                    break
                else:
                    height += int(grid[j][i])
                j -= 1
            heights.append(height)
        return heights
        
s = Solution()
s.maximalRectangle(
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
)