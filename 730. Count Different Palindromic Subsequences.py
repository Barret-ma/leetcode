# Given a string S, find the number of different non-empty palindromic 
# subsequences in S, and return that number modulo 10^9 + 7.

# A subsequence of a string S is obtained by deleting 0 or more characters from S.

# A sequence is palindromic if it is equal to the sequence reversed.

# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

# Example 1:
# Input: 
# S = 'bccb'
# Output: 6
# Explanation: 
# The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
# Example 2:
# Input: 
# S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# Output: 104860361
# Explanation: 
# There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
# Note:

# The length of S will be in the range [1, 1000].
# Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = len(S)
        M = 1e9 + 7
        dp = [[False for _ in range(l)] for _ in range(l)]
        for i in range(l):
            dp[i][i] = 1
        for k in range(1, l):
            for i in range(l - k):
                j = i + k
                if S[i] == S[j]:
                    left = i + 1
                    right = j - 1
                    while left <= right and S[left] != S[i]: left += 1
                    while left <= right and S[right] != S[i]: right -= 1
                    if left > right:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif left == right:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
                dp[i][j] = (dp[i][j] + M) if (dp[i][j] < 0) else dp[i][j] % M
        print(int(dp[0][l - 1]))
        return int(dp[0][l - 1])
s = Solution()
s.countPalindromicSubsequences('bccb')