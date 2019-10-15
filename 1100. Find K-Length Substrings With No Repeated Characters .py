class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        """
        unlock problem
        """
        if not s:
            return 0
        left = 0
        right = 0
        result = []
        hashMap = dict()
        while right < len(s):
            if s[right] in hashMap:
                left = right
                hashMap.clear()
            hashMap[s[right]] = right
            if right - left + 1 == k:
                result.append(s[left:right + 1])
                del hashMap[s[left]]
                left += 1
            right += 1

s = Solution()
s.numKLenSubstrNoRepeats('havefunonleetcode', 5)