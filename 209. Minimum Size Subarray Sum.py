# coding=UTF-8
# Given an array of n positive integers and a positive integer s, find the minimal 
# length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        left = 0
        right = 0
        count = 0
        minCnt = float('inf')
        while right < len(nums):
            count += nums[right]
            while left < right and count > s:
                if count - nums[left] >= s:
                    count -= nums[left]
                    left += 1
                else:
                    break

            if count >= s and minCnt > right - left + 1:
                minCnt = right - left + 1
            right += 1
        return (minCnt if (count >= s) else 0)
s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(10, [2,3,1]))