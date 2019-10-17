# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

class Solution(object):
    res = 0
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = 0
        for i in nums:
            total += i
        if total < S:
            return 0
        kOffset = total
        kMaxN = total * 2 + 1
        ways = [0 for _ in range(kMaxN)]
        ways[kOffset] = 1
        for num in nums:
            tmp = [0 for _ in range(kMaxN)]
            for i in range(num, kMaxN - num):
                tmp[i + num] += ways[i]
                tmp[i - num] += ways[i]
            ways = tmp
        return ways[S + kOffset]
s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
