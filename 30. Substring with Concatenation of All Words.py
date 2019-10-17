# You are given a string, s, and a list of words, words, 
# that are all of the same length. Find all starting indices 
# of substring(s) in s that is a concatenation of each word 
# in words exactly once and without any intervening characters.

 

# Example 1:

# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:

# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []
from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        word_len = len(words[0])
        word_total = (len(words) - 1) * word_len
        ans = []
        word_cnt = Counter(words)
        for i in range(word_len):
            start = i
            cur_cnt = Counter()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j: j + word_len]
                print(word)
                if word in word_cnt:
                    cur_cnt[word] += 1
                    while cur_cnt[word] > word_cnt[word]:
                        cur_cnt[s[start: start + word_len]] -= 1
                        start += word_len
                else:
                    cur_cnt.clear()
                    start = j + word_len
                
                if(start + word_total == j):
                    ans.append(start)
        return ans

s = Solution()
s.findSubstring('barfoothefoobarman', ["foo","bar"])