# Given two strings s1 and s2, write a function to return true if s2 contains 
# the permutation of s1. In other words, one of the first string's permutations 
# is the substring of the second string.

 

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 

# Note:

# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
from collections import defaultdict, Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 or not s2 or len(s1) > len(s2):
            return False
        
        left = 0
        right = 0
        # hashMap = defaultdict(lambda: 0)
        count = 0
        hashMap = Counter(s1)
        while (right < len(s2)):
            hashMap[s2[right]] -= 1
            if (hashMap[s2[right]] >= 0):
                count += 1

            while left < right and hashMap[s2[left]] < 0:
                hashMap[s2[left]] += 1
                left += 1
            if count == len(s1) and right - left + 1 == len(s1):
                return True
            right += 1
        return False

s = Solution()
# s.checkInclusion('ab', 'eidbaooo')
print(s.checkInclusion('abc', 'bbbca'))