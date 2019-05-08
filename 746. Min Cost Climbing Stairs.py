class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost) + 1
        dp = [0] * n
        for i in range(2, n):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[len(cost)]
s = Solution()
print s.minCostClimbingStairs([10, 15, 20])
print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print s.minCostClimbingStairs([0,0,1,1])
