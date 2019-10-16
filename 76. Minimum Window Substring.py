# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
from collections import defaultdict, Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ''
        left = 0
        right = 0
        minCnt = float('inf')
        # hashMap = defaultdict(lambda: 0)
        result = ''
        hashMap = Counter(t)
        count = 0
        while right < len(s):
            hashMap[s[right]] -= 1

            if (hashMap[s[right]] >= 0):
                count += 1

            while left < right and hashMap[s[left]] < 0:
                hashMap[s[left]] += 1
                left += 1
                
            if count == len(t) and minCnt > (right - left + 1):
                minCnt = right - left + 1
                result = s[left:right + 1]
            right += 1
        print(result)
        return result
            
s = Solution()
s.minWindow('ADOBECODEBANC', 'ABC')
# s.minWindow('aaflslflsldkalskaaa', 'aaa')
# s.minWindow('aa', 'aa')
            # while targetStrMap[s[right]] > 1:
            #     if s[left] in targetStrMap and targetStrMap[s[left]] > 1:
            #         left ++


            

            