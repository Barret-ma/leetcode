# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

# Example 1:

# Input: [1,3,5]
# Output: 1
# Example 2:

# Input: [2,2,2,0,1]
# Output: 0
# Note:

# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        left = 0
        right = len(nums) - 1
        res = nums[0]

        while left < right - 1:
            mid = left + (right - left) / 2
            if nums[left] < nums[mid]:
                res = min(res, nums[left])
                left = mid + 1

            elif nums[left] > nums[mid]:
                res = min(res, nums[right])
                right = mid
            else:
                left += 1

        res = min(res, nums[left])
        res = min(res, nums[right])
        return res
