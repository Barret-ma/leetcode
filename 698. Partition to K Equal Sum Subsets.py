# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Input: nums = [3, 3, 1, 5, 5, 2, 1]
 
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

# Note:

# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.

from collections import defaultdict

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """


        # countMap = defaultdict(lambda: 0)
        total = 0
        visited = [False] * len(nums)
        for i in range(len(nums)):
            total = total + nums[i]
            # countMap[n] = countMap[n] + 1

        if total % k != 0: return False
        average = total / k
        nums.sort()
        return self.helper(nums, k, average, 0, 0, visited)


    def helper(self, nums, k, target, start, curSum, visited):
        if k == 1:
            return True
        if curSum > target:
            return False
        if curSum == target:
            return self.helper(nums, k - 1, target, 0, 0, visited)
        for i in range(start, len(nums)):
            if visited[i]: continue
            visited[i] = True
            if self.helper(nums, k, target, i + 1, curSum + nums[i], visited):
                return True
            visited[i] = False



s = Solution()
s.canPartitionKSubsets([3, 3, 1, 5, 5, 2, 1], 4)

        
