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
        return results
    def dfs(self, s, arr, results):
        if len(arr) > 4:
            return
        if len(arr) == 4 and len(s) == 0:
            strIP = str(arr[0])
            for i in range(1, len(arr)):
                strIP = strIP + '.' + str(arr[i])
            results.append(strIP)
            return
        for i in range(1, len(s) + 1):
            currentIp = s[0:i]
            if currentIp[0] == '0' and len(currentIp) > 1:
                break
            num = int(currentIp)
            if num > 255:
                break
            else:
                if len(s[i:]) != 0 and len(arr) == 3:
                    continue
                self.dfs(s[i:], arr + [num], results)

s = Solution()
s.restoreIpAddresses('010010')