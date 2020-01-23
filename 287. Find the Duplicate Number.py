# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: [3,1,3,4,2]
# Output: 3
# Note:

# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # left = 1
        # right = len(nums)
        # while left < right:
        #     mid = left + (right - left) / 2
        #     cnt = 0
        #     for num in nums:
        #         if num <= mid:
        #             cnt += 1
        #     if cnt <= mid:
        #         left = mid + 1
        #     else: right = mid
        # return right
        slow = 0
        fast = 0
        t = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while True:
            slow = nums[slow]
            t = nums[t]
            if slow == t:
                break
        return slow

s = Solution()
s.findDuplicate([1,3,4,2,2])