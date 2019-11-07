#coding=UTF-8
# Given n balloons, indexed from 0 to n-1. Each balloon is painted 
# with a number on it represented by array nums. You are asked to burst 
# all the balloons. If the you burst balloon i you will get 
# nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent 
# indices of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons wisely.

# Note:

# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:

# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

from collections import deque
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dq = deque(nums)
        dq.append(1)
        dq.appendleft(1)
        l = len(nums)
        dp = [[0 for _ in range(l + 2)] for _ in range(l + 2)]
        for m in range(1, l + 1):
            for i in range(1, l - m + 2):
                j = i + m - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dq[i - 1] * dq[k] * dq[j + 1] + dp[i][k - 1] + dp[k + 1][j])
        return dp[1][l]

s = Solution()
s.maxCoins([3, 1, 5, 8])