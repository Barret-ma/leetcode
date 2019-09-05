# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 

# Example 1:

# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# Example 2:

# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]

# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
 

# Note:

# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
from collections import defaultdict
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return None
        yl = len(matrix)
        xl = len(matrix[0])

        for m in range(len(matrix)):
            row = matrix[m]
            for n in range(len(row)):
                if row[n] != 0:
                    visited = defaultdict(lambda:{})
                    row[n] = self.visit(matrix, m, n, xl, yl, 0, visited)
        return matrix
    def visit(self, g, x, y, xsize, ysize, distance, visited):
        if x < 0 or y < 0 or x > ysize - 1 or y > xsize - 1 or (y in visited[x] and visited[x][y] == 1):
            return float('inf')
        else:
            if g[x][y] == 0:
                return distance
            else:
                visited[x][y] = 1
                d1 = self.visit(g, x + 1, y, xsize, ysize, distance + 1, visited)
                d2 = self.visit(g, x - 1, y, xsize, ysize, distance + 1, visited)
                d3 = self.visit(g, x, y + 1, xsize, ysize, distance + 1, visited)
                d4 = self.visit(g, x, y - 1, xsize, ysize, distance + 1, visited)
                # visited[x][y] = None
        return min(d1, d2, d3, d4)
s = Solution()
print(s.updateMatrix(
    [[0,0,1,0,1,2,1,0,1,7],
    [1,1,2,1,0,1,1,1,2,6],
    [2,1,2,1,1,0,0,0,1,5],
    [1,0,1,0,1,1,1,0,1,4],
    [0,0,1,1,1,0,1,1,2,3],
    [1,0,1,2,1,1,1,2,1,2],
    [1,1,1,1,0,1,0,1,0,1],
    [0,1,0,0,0,1,0,0,1,2],
    [1,1,1,0,1,1,0,1,0,1],
    [1,0,1,1,1,0,1,2,1,0]]
))