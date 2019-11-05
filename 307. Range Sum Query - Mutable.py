# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# The update(i, val) function modifies nums by updating the element at index i to val.

# Example:
# Given nums = [1, 3, 5]

# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.
class NumArray(object):
    data = []
    bit = []
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.data = [0] * n
        self.bit = [0]  * (n + 1)
        for i in range(n):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        diff = val - self.data[i]
        j = i + 1
        while j < len(self.bit):
            self.bit[j] += diff
            j += (j & -j)
        self.data[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j + 1) - self.getSum(i)
    def getSum(self, i):
        res = 0
        j = i
        while j > 0:
            res += self.bit[j]
            j -= (j & -j)
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

s = NumArray([1, 3, 5])
s.update(2, 10)


