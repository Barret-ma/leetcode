# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        # ans = 0
        for i in range(1, n):
            mx = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    mx = max(mx, dp[j] + 1)
            dp[i] = mx
        return max(dp)

s = Solution()
# s.lengthOfLIS([10,9,2,5,3,7,101,18])
# s.lengthOfLIS([1,5,2,6,3,7,4,8])
print(s.lengthOfLIS([1, 1, 1]))
# print s.lengthOfLIS([1,0])