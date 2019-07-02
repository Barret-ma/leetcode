# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Example 1:

# Input: [0,1,0]
# Output: 1
# Example 2:

# Input: [0,2,1,0]
# Output: 1
# Note:

# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return
        length = len(A)
        left = 0
        right = length
        while left < right:
            mid = left + (right - left) / 2
            if mid == 0 or mid == length - 1:
                return mid
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid

            elif A[mid] < A[mid + 1] and A[mid] > A[mid - 1]:
                left = mid + 1
            else:
                right = mid
        return right

s = Solution()
print(s.peakIndexInMountainArray([5,2,1,0]))