# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        l = len(nums)
        if l == 1:
            return nums[0]
        i = 1
        pre = nums[0]
        while i < l - 1 and pre < nums[i]:
            pre = nums[i]
            i += 1
        if i == l - 1 and pre < nums[i]:
            return nums[0]
        return nums[i]

s = Solution()
print(s.findMin([0]))