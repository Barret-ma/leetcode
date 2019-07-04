# A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

# What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

# Examples:
# Input: A = [1, 2, 3, 5], K = 3
# Output: [2, 5]
# Explanation:
# The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
# The third fraction is 2/5.

# Input: A = [1, 7], K = 1
# Output: [1, 7]
# Note:

# A will have length between 2 and 2000.
# Each A[i] will be between 1 and 30000.
# K will be between 1 and A.length * (A.length - 1) / 2.


class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        if not A:
            return
        length = len(A)
        left = 0
        right = 1
        p = 0
        q = 1
        cnt = 0
        while True:
            mid = left + (right - left) / 2.0
            cnt = 0
            p = 0
            j = 0
            for i in range(length):
                while j < length and A[i] > mid * A[j]:
                    j += 1
                cnt += length - j
                if j < length and p * A[j] < q * A[i]:
                    p = A[i]
                    q = A[j]
                # cnt +=
            if cnt == K:
                return [p, q]
            elif cnt < K:
                left = mid
            else:
                right = mid
