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
        n = len(A)
        left = 0
        right = 1.0

        while left < right:
            mid = (left + right) / 2.0
            total = 0
            p = 0
            q = 0
            maxF = 0.0
            j = 1
            for i in range(n - 1):
                while j < n and A[i] > mid * A[j]:
                    j += 1
                if n == j:
                    break
                total += n - j
                f = float(A[i]) / A[j]
                if f > maxF:
                    p = A[i]
                    q = A[j]
                    maxF = f
            if total == K:
                return [p, q]
            elif total < K:
                left = mid
            else:
                right = mid


s = Solution()
print(s.kthSmallestPrimeFraction([1, 13, 17, 59], 6))
