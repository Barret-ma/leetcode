# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

# Example 1:

# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0
        la = len(A)
        lb = len(B)
        dp = [[0 for _ in range(la + 1)] for _ in range(lb + 1)]
        maxCnt = 0
        for i in range(la + 1):
            for j in range(lb + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if A[i - 1] == B[j - 1]:
                        print(i)
                        print(j)
                        dp[i][j] = dp[i - 1][j - 1] + 1
                        maxCnt = max(maxCnt, dp[i][j])

        return maxCnt

s = Solution()
s.findLength([1,2,3,2,1], [3,2,1,4,7])
