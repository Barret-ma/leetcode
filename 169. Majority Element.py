# coding=UTF-8
# Given an array of size n, find the majority element. The majority 
# element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element 
# always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # nums.sort()
        # current = nums[0]
        # total = 1
        # for i in range(1, n):
        #     if nums[i] == current:
        #         total += 1
        #         if total > (n / 2):
        #             return current
        #     else:
        #         current = nums[i]
        #         total = 1
        res = 0
        cnt = 0
        for num in nums:
            if cnt == 0:
                res = num
                cnt += 1
            else:
                cnt = cnt + 1 if res == num else cnt - 1
        return res
                
        

s = Solution()
print(s.majorityElement([1,1,1,1,1]))

