# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets such 
# that the sum of elements in both subsets is equal.

# Note:

# Each of the array element will not exceed 100.
# The array size will not exceed 200.
 

# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        total = 0
        for num in nums:
            total += num
        if total % 2 != 0:
            return False
        target = total / 2
        dp = [False for _ in range(target + 1)]

        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]


        

s = Solution()
print(s.canPartition([1, 2, 3, 4, 5, 6, 7]))
