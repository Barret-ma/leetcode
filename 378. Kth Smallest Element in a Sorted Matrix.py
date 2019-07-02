# coding=UTF-8
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return
        l = len(matrix)
        left = matrix[0][0]
        right = matrix[l-1][l-1]
        cnt = 0
        while left < right:
            mid = left + (right - left) / 2
            cnt = 0
            for i in range(l):
                cnt += self.upperBound(matrix[i], mid) - 0
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left

    def upperBound(self, nums, target):
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return right


s = Solution()
print(s.kthSmallest([
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
], 8))
