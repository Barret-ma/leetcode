# Given a non-empty string s and a dictionary wordDict containing a list 
# of non-empty words, add spaces in s to construct a sentence where each 
# word is a valid dictionary word. Return all such possible sentences.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:

# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
from collections import defaultdict

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        m = defaultdict(lambda: [])
        return self.helper(s, wordDict, m)

    def helper(self, s, wordDict, m):
        if m[s]:
            return m[s]
        if not s:
            return ""
        res = []
        for word in wordDict:
            if s[0: len(word) + 1] != word: continue
            rem = self.helper(s[len(word) + 1:], wordDict, m)
            for str in rem:
                res.append(word + ("" if not len(str) else str))
        m[s] = res
        return m[s]
s = Solution()
print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))