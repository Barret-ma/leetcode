# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        mh = len(matrix)
        if mh == 0: return 0
        mw = len(matrix[0])
        sizes = [[0 for _ in range(mw)] for _ in range(mh)]
        ans = 0
        for i in range(mh):
            for j in range(mw):
                sizes[i][j] = int(matrix[i][j])
                if not sizes[i][j]: continue
                if i == 0 or j == 0:
                    pass
                elif i == 0:
                    sizes[i][j] = sizes[i][j - 1] + 1
                elif j == 0:
                    sizes[i][j] = sizes[i - 1][j] + 1
                else:
                    sizes[i][j] = min(min(sizes[i - 1][j - 1], sizes[i - 1][j]), sizes[i][j - 1]) + 1
                ans = max(ans, sizes[i][j] * sizes[i][j])
        print(ans)
        return ans

s = Solution()
s.maximalSquare(
    [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
)