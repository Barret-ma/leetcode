# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2]
#         0 1 2 3 4
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
        # if not nums:
        #     return
        # l = len(nums)
        # if l == 1:
        #     return nums[0]
        # i = 1
        # pre = nums[0]
        # while i < l - 1 and pre < nums[i]:
        #     pre = nums[i]
        #     i += 1
        # if i == l - 1 and pre < nums[i]:
        #     return nums[0]
        # return nums[i]

        if not nums:
            return
        l = len(nums)
        left = 0
        right = l - 1
        if nums[left] > nums[right]:
            while left != right - 1:
                mid = (left + right) / 2
                if nums[mid] > nums[left]:
                    left = mid
                else:
                    right = mid
            return min(nums[left], nums[right])
        return nums[0]
        

s = Solution()
print(s.findMin([10,1,10,10,10]))