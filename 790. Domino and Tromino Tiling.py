class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        kMod = 1e9 + 7
        dp = [[0, 0] for _ in range(N + 1)]
        dp[0][0] = dp[1][0] = 1
        for i in range(2, (N + 1)):
            dp[i][0] = int((dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 1][1]) % kMod)
            dp[i][1] = int((dp[i - 2][0] + dp[i - 1][1]) % kMod)
        return dp[N][0]

s = Solution()
print(s.numTilings(3))