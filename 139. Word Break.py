# Given a non-empty string s and a dictionary wordDict containing a 
# list of non-empty words, determine if s can be segmented into a 
# space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dictSet = set(wordDict)
        dp = [0] * (len(s) + 1)
        dp[0] = True
        for i in range(len(dp)):
            for j in range(i):
                print(s[j:i])
                if dp[j] and s[j:i] in dictSet:
                    dp[i] = True
                    break
        return dp.pop()

s = Solution()
# print(s.wordBreak("leetcode", ["leet", "code"]))
print(s.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))

