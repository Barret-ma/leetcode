# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different 
# substrings even they consist of same characters.

# Example 1:

# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
 

# Example 2:

# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Note:

# The input string length won't exceed 1000.


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s:
        #     return 0
        # l = len(s)
        # self.res = 0

        # def helper(s, i, j):
        #     while i >= 0 and j < len(s) and s[i] == s[j]:
        #         i -= 1
        #         j += 1
        #         self.res += 1

        # for i in range(l):
        #     helper(s, i, i)
        #     helper(s, i, i + 1)
        # return self.res
        l = len(s)
        dp = [[False for _ in range(l)] for _ in range(l)]
        self.res = 0
        for i in range(l - 1, -1, -1):
            for j in range(i, l):
                dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j]:
                    self.res += 1
        return self.res

s = Solution()
s.countSubstrings('aaa')
