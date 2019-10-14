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
        window = []
        res = 0
        visitMap = defaultdict(lambda: None)
        for i in range(len(s)):
            print(s[i])
            if (s[i] not in visitMap):
                visitMap[s[i]] = True
                window.append(s[i])
                # res = max(res, len(window))
            else:
                res = max(res, len(window))
                window = []
                window.append(s[i])

                pass
                

s = Solution()
s.lengthOfLongestSubstring('abcabcbb')
