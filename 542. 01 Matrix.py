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
from Queue import Queue
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        q = Queue()
        ysize = len(matrix)
        xsize = len(matrix[0])
        dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        for i in range(ysize):
            row = matrix[i]
            for j in range(xsize):
                if row[j] != 0:
                    row[j] = float('inf')
                else:
                    q.put([i, j])
        while not q.empty():
            top = q.get()
            for dir in dirs:
                x = top[0] + dir[0]
                y = top[1] + dir[1]
                if x < 0 or y < 0 or x >= ysize or y >= xsize or matrix[top[0]][top[1]] >= matrix[x][y]:
                    continue
                matrix[x][y] = matrix[top[0]][top[1]] + 1
                q.put([x, y])
        return matrix


        