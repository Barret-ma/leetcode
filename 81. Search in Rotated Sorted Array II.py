# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        if not nums:
            return
        l = len(nums)
        if l == 1:
            return nums[0] == target
        i = 1
        pre = nums[0]
        while i < l - 1 and pre <= nums[i]:
            pre = nums[i]
            i += 1
        if nums[i] == target:
            return True
        elif nums[i - 1] >= target and target >= nums[0]:
            return self.binarySearch(nums[0:i], target)
        else:
            return self.binarySearch(nums[i + 1:len(nums)], target)

    def binarySearch(self, nums, target):
        # while left < right:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        mid = len(nums) / 2
        if nums[mid] == target:
            return True
        else:
            if nums[mid] > target:
                return self.binarySearch(nums[0:mid], target)
            else:
                return self.binarySearch(nums[mid + 1:len(nums)], target)


s = Solution()
print(s.search([2, 6], 6))
