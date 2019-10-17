# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        window = []
        res = 0
        visitMap = defaultdict(lambda: None)
        i = 0
        while i < len(s):
            if (s[i] not in visitMap):
                visitMap[s[i]] = i
                window.append(s[i])
                # res = max(res, len(window))
            else:
                i = visitMap[s[i]]
                res = max(res, len(window))
                window = []
                visitMap.clear()
                # visitMap[s[i]] = True
                # window.append(s[i])
            i += 1
        res = max(res, len(window))
        return res
                

s = Solution()
s.lengthOfLongestSubstring('abcabcbb')
