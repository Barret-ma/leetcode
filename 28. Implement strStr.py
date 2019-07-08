class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        if not needle or haystack == needle:
            return 0
        for i in range(len(haystack) - 1):
            if haystack[i] == needle[0]:
                if needle == haystack[i: i + len(needle)]:
                    return i
        return -1


test = Solution()

print test.strStr('a', 'a')