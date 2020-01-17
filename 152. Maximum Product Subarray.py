# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        # dp = [0 for _ in range(n)]
        # dp[0] = nums[0]

        mx = nums[0]
        mn = nums[0]
        res = nums[0]
        for i in range(n):
            tmax = mx
            tmin = mn
            mx = max(max(nums[i], tmax * nums[i]), tmin * nums[i])
            mn = min(min(nums[i], tmax * nums[i]), tmin * nums[i])
            res = max(res, mx)

        return res

s = Solution()
print(s.maxProduct([2,3,-2,4]))