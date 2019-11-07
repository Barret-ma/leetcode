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
    m = defaultdict(lambda: list)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # words = set(wordDict)
        # mem = {}
        # def wordBreak(s):
        #     if s in mem:
        #         return mem[s]
        #     ans = []
        #     if s in words:
        #         ans.append(s)
        #     for i in range(1, len(s)):
        #         right = s[i:]
        #         if right not in words: continue
        #         ans += []
        self.m = defaultdict(lambda: list)
        return self.helper(s, wordDict)
    def helper(self, s, wordDict):
        if s in self.m:
            return self.m[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[0:len(word)] != word:
                continue
            rem = self.helper(s[len(word):], wordDict)
            for s1 in rem:
                res.append(word + ("" if not s1 else " " + s1))
        self.m[s] = res
        return self.m[s]
        
s = Solution()
print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
# print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "s", "an", "d"]))