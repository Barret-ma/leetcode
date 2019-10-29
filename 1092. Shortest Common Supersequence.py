# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

# (A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

# Example 1:

# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.
 

# Note:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.
from collections import deque
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1)
        l2 = len(str2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        ans = deque()
        while l1 or l2:
            if l1 == 0:
                l2 -= 1
                c = str2[l2]
            elif l2 == 0:
                l1 -= 1
                c = str1[l1]
            elif str1[l1 - 1] == str2[l2 - 1]:
                l1 -= 1
                l2 -= 1
                c = str1[l1]
            elif dp[l1 - 1][l2] == dp[l1][l2]:
                l1 -= 1
                c = str1[l1]
            elif dp[l1][l2 - 1] == dp[l1][l2]:
                l2 -= 1
                c = str2[l2]
            ans.appendleft(c)
        return ''.join(ans)

s = Solution()
s.shortestCommonSupersequence('bbcbcaabc', 'cacaabaaaa')
# bbcabcaabaaaac