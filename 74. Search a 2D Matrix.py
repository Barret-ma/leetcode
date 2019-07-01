# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return

        matrixLength = len(matrix)
        itemLength = len(matrix[0])
        totalLength = matrixLength * itemLength

        left = 0
        right = totalLength

        while left < right:
            mid = left + (right - left) / 2
            rowsIndex = (mid % itemLength)
            columnIndex = mid / itemLength
            if matrix[columnIndex][rowsIndex] == target:
                return True
            elif matrix[columnIndex][rowsIndex] < target:
                left = mid + 1
            else:
                right = mid
        return False


s = Solution()
print(s.searchMatrix(
    [
        [1],
        [3]
    ], 1
))
