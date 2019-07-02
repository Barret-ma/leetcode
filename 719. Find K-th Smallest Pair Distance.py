# Given an integer array, return the k-th smallest distance among all the pairs.
# The distance of a pair (A, B) is defined as the absolute difference between A and B.

# Example 1:
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Note:
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return
        nums.sort()
        print(nums)
        length = len(nums)
        left = 0
        right = nums[length - 1] - nums[0]
        while left < right:
            mid = left + (right - left) / 2
            cnt = 0
            start = 0
            for i in range(length):
                while start < length and nums[i] - nums[start] > mid:
                    start += 1
                cnt += i - start
            if cnt < k:
                left = mid + 1

            else:
                right = mid
        return right


s = Solution()
print(s.smallestDistancePair([38, 33, 57, 65, 13, 2, 86, 75, 4, 56], 26))
