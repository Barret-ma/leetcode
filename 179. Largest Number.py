# Given a list of non negative integers, arrange them such that they form the largest number.

# Example 1:

# Input: [10,2]
# Output: "210"
# Example 2:

# Input: [3,30,34,5,9]
# Output: "9534330"
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        self.quickSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums)))) 
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
            
    def quickSort(self, nums, l, r):
        if l >= r:
            return 
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos-1)
        self.quickSort(nums, pos+1, r)
        
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low