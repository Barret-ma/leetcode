# Given an array nums, we call (i, j) an important 
# reverse pair if i < j and nums[i] > 2*nums[j].

# You need to return the number of important reverse pairs in the given array.

# Example1:

# Input: [1,3,2,3,1]
# 1, 1, 2, 3, 3
# Output: 2
# Example2:

# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
# class BIT:
#     def __init__(self, n):
#         self.n = n + 1
#         self.sums = [0] * self.n
    
#     def update(self, i, delta):
#         while i < self.n:
#             self.sums[i] += delta
#             i += i & (-i)
    
#     def query(self, i):
#         res = 0
#         while i > 0:
#             res += self.sums[i]
#             i -= i & (-i)
#         return res
# class Solution(object):
#     def reversePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # BIT O(nlogn)
#         new_nums = nums + [x * 2 for x in nums]
#         sorted_set = sorted(list(set(new_nums)))
#         tree = BIT(len(sorted_set))
#         res = 0
#         ranks = {}
#         for i, n in enumerate(sorted_set):
#             ranks[n] = i + 1

#         for n in nums[::-1]:
#             res += tree.query(ranks[n] - 1)
#             tree.update(ranks[n * 2], 1)

#         return res

import copy
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        v = copy.deepcopy(nums)
        bit = [0] * (n + 1)
        v.sort()
        m = dict()
    # [1,1,2,3,3]
#      0,1,2,3,4
        def lower_bound(arr, target):
            low, high = 0, len(arr) - 1
            pos = len(arr)
            while low<high:
                mid = (low+high)/2 
                if arr[mid] < target:
                    low = mid+1
                else:#>=
                    high = mid
                    #pos = high
            if arr[low]>=target:
                pos = low
            return pos

        for i in range(n):
            m[v[i]] = i + 1
        print(m)
        for i in range(n - 1, -1, -1):
            res += self.getSum(lower_bound(v, nums[i] / 2.0) - 0, bit)
            self.update(m[nums[i]], bit)
        print(bit)
        return res

    def getSum(self, i, bit):
        sum = 0
        while (i > 0):
            sum += bit[i]
            i -= (i & -i)
        return sum
    def update(self, i, bit):
        while i < len(bit):
            bit[i] += 1
            i += (i & -i)
s = Solution()
print(s.reversePairs([1,3,2,3,1]))