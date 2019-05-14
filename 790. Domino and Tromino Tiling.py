class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        kMod = int(1e9 + 7)
        dp = [[0,0]] * (N + 1)
        print(dp)
        dp[0][0] = dp[1][0] = 1

        for i in range(2, N + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 1][1]) % kMod
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][1]) % kMod
        print dp
        return dp[N][0]

s = Solution()
print(s.numTilings(3))