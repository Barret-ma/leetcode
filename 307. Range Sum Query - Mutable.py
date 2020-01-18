# coding=UTF-8
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
    # 
    #   BIT Solution
    # 
    # data = []
    # bit = []
    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     """
    #     n = len(nums)
    #     self.data = [0] * n
    #     self.bit = [0]  * (n + 1)
    #     for i in range(n):
    #         self.update(i, nums[i])

    # def update(self, i, val):
    #     """
    #     :type i: int
    #     :type val: int
    #     :rtype: None
    #     """
    #     diff = val - self.data[i]
    #     j = i + 1
    #     while j < len(self.bit):
    #         self.bit[j] += diff
    #         j += (j & -j)
    #     self.data[i] = val
        

    # def sumRange(self, i, j):
    #     """
    #     :type i: int
    #     :type j: int
    #     :rtype: int
    #     """
    #     return self.getSum(j + 1) - self.getSum(i)
    # def getSum(self, i):
    #     res = 0
    #     j = i
    #     while j > 0:
    #         res += self.bit[j]
    #         j -= (j & -j)
    #     return res

    # 
    #   BIT Solution
    #


    # 
    #   Segment Solution
    #  

    def __init__(self, nums):
        n = len(nums)
        self.segTree = [0] * n * 2
        self.nums = nums
        self.build(0, n - 1, 0)
        print(self.segTree)

    def build(self, start, end, i):
        if start == end:
            self.segTree[i] = self.nums[start]
        else:
            mid = (start + end) / 2
            self.build(start, mid, 2 * i + 1)
            self.build(mid + 1, end, 2 * i + 2)
            self.segTree[i] = self.segTree[2 * i + 1] + self.segTree[2 * i + 2]
    def update(self, i, val):
        self.updateIdx(0, len(self.nums) - 1, i, val, 0)
        print(self.segTree)

    def updateIdx(self, start, end, i, val, id):
        if start == end:
            self.segTree[id] = val
            return
        mid = (start + end) / 2
        if i <= mid:
            self.updateIdx(start, mid, i, val, 2 * id + 1)
        else:
            self.updateIdx(mid + 1, end, i, val, 2 * id + 2)
        self.segTree[id] = self.segTree[2 * id + 1] + self.segTree[2 * id + 2]
    def sumRange(self, i, j):
        return self.sumRangeIdx(0, len(self.nums) - 1, i, j, 0)
    def sumRangeIdx(self, start, end, i, j, id):
        if start > j or end < i:
            return 0
        if i <= start and j >= end:
            return self.segTree[id]
        mid = (start + end) / 2
        return self.sumRangeIdx(start, mid, i, j, 2 * id + 1) + self.sumRangeIdx(mid + 1, end, i, j, 2 * id + 2)
    # 
    #   Segment Solution
    #
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

s = NumArray([1, 3, 5, 7])
s.update(1, 2)
print(s.sumRange(1,3))


