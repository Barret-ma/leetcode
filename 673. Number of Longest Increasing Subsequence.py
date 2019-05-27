
# Given an unsorted array of integers, find the number of longest
#  increasing subsequence.

# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, 
# and there are 5 subsequences' length is 1, so output 5.
# Note: Length of the given array will be not exceed 2000 and the answer is 
# guaranteed to be fit in 32-bit signed int.

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        l = [1] * n
        cnt = [1] * n
        mx = 0
        res = 0
        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]: continue
                if l[i] == l[j] + 1:
                    cnt[i] = cnt[i] + cnt[j]
                elif l[i] < l[j] + 1:
                    l[i] = l[j] + 1
                    cnt[i] = cnt[j]
            if  mx == l[i]: res += cnt[i]
            elif mx < l[i]:
                mx = l[i]
                res = cnt[i]
        return res

s = Solution()
# print(s.findNumberOfLIS([1,3,5,4,7]))
# print(s.findNumberOfLIS([2,2,2,2,2]))

print(s.findNumberOfLIS([1,2,4,3,5,4,7,2]))




    
        