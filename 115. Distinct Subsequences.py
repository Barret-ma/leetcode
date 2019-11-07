
# coding=UTF8
# Given a string S and a string T, count the number 
# of distinct subsequences of S which equals T.

# A subsequence of a string is a new string which is 
# formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of 
# the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Example 1:

# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:

# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)

# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# Example 2:

# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:

# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)

# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^


class Solution(object):
    total = 0
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
    #     self.total = 0
    #     l1 = len(s)
    #     l2 = len(t)
    #     self.dfs(s, t)
    #     print(self.total)
    #     return self.total
    # def dfs(self, s, t):
    #     count = 0
    #     if t == '':
    #         self.total += 1
    #         return
    #     for s1 in s:
    #         count += 1
    #         if len(s[count:]) < len(t) - 1:
    #             break
    #         if s1 == t[0]:
    #             self.dfs(s[count:], t[1:])

        l1 = len(s)
        l2 = len(t)
        dp = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
        for j in range(l1 + 1):
            dp[0][j] = 1
        print(dp)
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                dp[i][j] = dp[i][j - 1] + (dp[i - 1][j - 1] if s[j - 1] == t[i - 1] else 0)

        return dp[l2][l1]




s = Solution()
print(s.numDistinct('rabbbit', 'rabbit'))