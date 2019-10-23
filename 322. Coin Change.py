# coding=UTF-8
# You are given coins of different denominations 
# and a total amount of money amount. Write a function 
# to compute the fewest number of coins that you need 
# to make up that amount. If that amount of money cannot 
# be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

# dp[i] 为 i面值需要硬币的个数

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if not coins:
            return -1
        dp = [float('inf') for _ in range(amount + 1)]
        for coin in coins:
            if coin > amount:
                continue
            dp[coin] = 1
        for i in range(amount + 1):
            minCnt = float('inf')
            for coin in coins:
                if i - coin >= 0 :
                    minCnt = min(minCnt, dp[coin] + dp[i - coin])
            dp[i] = min(minCnt, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1


s = Solution()
print(s.coinChange([1,2147483647], 2))