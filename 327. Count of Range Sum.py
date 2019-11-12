#coding=UTF-8
# Given an integer array nums, return the number of 
# range sums that lie in [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the 
# elements in nums between indices i and j (i ≤ j), inclusive.

# Note:
# A naive algorithm of O(n2) is trivial. You MUST do better than that.

# Example:

# Input: nums = [-2,5,-1], lower = -2, upper = 2,
# Output: 3 
# Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
import copy
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        v = copy.deepcopy(nums)
        l = len(nums)
        v.sort()
        if v[l - 1] < lower or v[0] > upper:
            return 0
        result = []
        def dfs(arr, total):
            for i in range(len(arr)):
                result.append(arr[i] + total)
                dfs(arr[i + 1:], arr[i] + total)

        dfs(nums, 0)
        result.sort()
        print(result)
        l1 = len(result)
        res = 0
        bit = [0] * (l1 + 1)
        for i in range(l1):
            if result[i] >= lower and result[i] <= upper:
                res += self.getSum(i + 1, bit)
                self.update(i + 1, bit)
    def update(self, i, bit):
        while i < len(bit):
            bit[i] += 1
            i += (i & -i)
    def getSum(self, i, bit):
        total = 0
        while i > 0:
            total += bit[i]
            i -= (i & -i)
        return total
        

s = Solution()
s.countRangeSum([-2,5,-1], -2, 2)