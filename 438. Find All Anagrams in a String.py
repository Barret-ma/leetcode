# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# from collections import Counter
from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#         if not s:
#             return []
#         pLen = len(p)
#         left = 0
#         right = 0
#         results = []
#         hashMap = Counter(p)
#         count = len(p)

#         while right < len(s):
#             hashMap[s[right]] -= 1
#             if hashMap[s[right]] >= 0:
#                 count -= 1
#             while (right - left + 1 > pLen or hashMap[s[left]] < 0) and left < right:
#                 hashMap[s[left]] += 1
#                 if s[left] in p and hashMap[s[left]] > 0:
#                     count += 1
#                 left += 1
#             if right - left + 1 == pLen and count == 0:
#                 results.append(left)
#             right += 1
#         print(results)
#         return results

        if not s or not p:
            return []
        sArr = list(s)
        pArr = list(p)
        hashMap = defaultdict(lambda: 0)
        for letter in pArr:
            hashMap[letter] += 1
            
        left = 0
        count = 0
        size = len(pArr)
        ans = []
        for right in range(len(sArr)):
            hashMap[sArr[right]] -= 1
            if hashMap[sArr[right]] >= 0:
                count += 1
            if right - left + 1 >  size:
                hashMap[sArr[left]] += 1
                if (hashMap[sArr[left]] > 0):
                    count -= 1
                left += 1
            if count == size:
                ans.append(left)
                
        return ans

s = Solution()
# s.findAnagrams('cbaebacbacd', 'abc')
# s.findAnagrams('baxxxaa', 'aa')
print(s.findAnagrams('abab', 'ab'))