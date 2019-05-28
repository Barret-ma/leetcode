# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        dp = [[-1] * (l2 + 1) for _ in range(l1 + 1)]
        print(dp)
        return self.findMinDistance(dp, word1, word2, l1, l2)


    def findMinDistance(self, dp, word1, word2, l1, l2):
        if l1 == 0: return l2
        if l2 == 0: return l1
        if dp[l1][l2] >= 0:
            return dp[l1][l2]
        if word1[l1 - 1] == word2[l2 - 1]:
            ans = self.findMinDistance(dp, word1, word2, l1 - 1, l2 - 1)
        else:
            ans = min(self.findMinDistance(dp, word1, word2, l1 - 1, l2 - 1), self.findMinDistance(dp, word1, word2, l1 - 1, l2), self.findMinDistance(dp, word1, word2, l1, l2 - 1)) + 1
        
        dp[l1][l2] = ans
        return ans

# s = Solution()
# print(s.minDistance("horse", "ros"))