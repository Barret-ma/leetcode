# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# Example:

# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

from collections import deque

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = []
        self.dfs(s, [], results)
        print results
        return results
    def dfs(self, s, partitionArr, results):
        if (len(s) == 0):
            results.append(partitionArr)
            return
        for i in range(1, len(s) + 1):
            currentStr = s[0:i]
            if self.isPalindrome(currentStr):
                self.dfs(s[i:], partitionArr + [currentStr], results)
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        else:
            dequeStr = deque(s)
            l = len(dequeStr)
            while l > 0:
                if dequeStr.popleft() != dequeStr.pop():
                    return False
                elif len(dequeStr) == 1 or len(dequeStr) == 0:
                    return True
s = Solution()
s.partition('aabb')

