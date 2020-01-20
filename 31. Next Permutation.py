# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                for j in range(n - 1, i, -1):
                    if nums[j] > nums[i]:
                        break
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = reversed(nums[i + 1:])
                return

        nums.reverse()
        print(nums)
            

s = Solution()
s.nextPermutation([3,2,1])