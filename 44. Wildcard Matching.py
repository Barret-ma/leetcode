#
# @lc app=leetcode id=44 lang=python
#
# [44] Wildcard Matching
#
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        iStar = -1
        jStar = -1
        while i < len(s):
            if s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
            elif p[j] == '*':
                iStar = i
                jStar = j
                j += 1
            elif iStar >= 0:
                iStar += 1
                i = iStar
                j = iStar + 1
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
s = Solution()
print(s.isMatch('adceb', '*a*b'))