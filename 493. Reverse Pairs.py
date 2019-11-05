# Given an array nums, we call (i, j) an important 
# reverse pair if i < j and nums[i] > 2*nums[j].

# You need to return the number of important reverse pairs in the given array.

# Example1:

# Input: [1,3,2,3,1]
# Output: 2
# Example2:

# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        v = nums
        bit = [0] * (n + 1)
        v.sort()
        m = dict()

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
        for i in range(n - 1, 0, -1):
            res += self.getSum(lower_bound(nums, nums[i] / 2.0) - v[0], bit)
            self.update(m[nums[i]], bit)
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