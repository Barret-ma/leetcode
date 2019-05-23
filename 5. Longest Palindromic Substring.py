# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        l = len(s)
        dp = [[0] * l for _ in range(l)]
        left = 0
        right = 0
        length = 0
        for i in range(l):
            dp[i][i] = 1
            for j in range(i):
                dp[j][i] = (s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]))
                if dp[j][i] and length < i - j + 1:
                    length = i - j + 1
                    left = j
                    right = i

        return s[left:right + 1]

s = Solution()
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("babad"))