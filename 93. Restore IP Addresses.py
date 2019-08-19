# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# Example:

# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        self.dfs(s, [], results)
        print results
        return results
    def dfs(self, s, arr, results):
        if len(arr) > 4:
            return
        if len(arr) == 4 and len(s) == 0:
            print arr
            results.append(arr)
            return
        elif len(arr) == 4 and len(s) != 0:
            return
        for i in range(1, len(s)):
            num = int(s[0:i])
            if num > 255:
                continue
            else:
                self.dfs(s[i:], arr + [num], results)



s = Solution()
s.restoreIpAddresses('25525511135')

