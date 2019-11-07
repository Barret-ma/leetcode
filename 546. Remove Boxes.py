# Given several boxes with different colors represented 
# by different positive numbers.
# You may experience several rounds to remove boxes until 
# there is no box left. Each time you can choose some continuous 
# boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
# Find the maximum points you can get.

# Example 1:
# Input:

# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# Output:
# 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
# Note: The number of boxes n would not exceed 100.

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        N = len(boxes)
        memo = [[[0]*N for _ in xrange(N) ] for _ in xrange(N) ]
    
        def dp(i, j, k):
            if i > j: return 0
            if not memo[i][j][k]:
                m = i
                while m+1 <= j and boxes[m+1] == boxes[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i+1, j, 0) + (k+1) ** 2
                for m in xrange(i+1, j+1):
                    if boxes[i] == boxes[m]:
                        ans = max(ans, dp(i+1, m-1, 0) + dp(m, j, k+1))
                memo[i][j][k] = ans
            return memo[i][j][k]
    
        return dp(0, N-1, 0)

s = Solution()
print(s.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))