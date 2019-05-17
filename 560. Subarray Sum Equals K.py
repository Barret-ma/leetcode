# Given an array of integers and an integer k, you need to 
# find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the 
# range of the integer k is [-1e7, 1e7].

import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        ans = 0
        sum = 0
        counts = collections.defaultdict(lambda: 0)
        counts[0] = 1
        for num in nums:
            sum += num
            print(sum - k)
            ans += counts[sum - k]
            counts[sum] += 1
        return ans


s = Solution()

print(s.subarraySum([1, 1, 1], 2))