import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # res = 0
        # c = collections.Counter(nums)
        # for i in c:
        #     if k > 0 and i + k in c or k == 0 and c[i] > 1:
        #         res += 1
        # return res


        res = 0
        n = len(nums)
        j = 0
        i = 0
        nums.sort()
        while i < n:
            j = max(j, i + 1)
            while ( j < n and nums[j] - nums[i] < k): j += 1
            if (j < n and nums[j] - nums[i] == k): res += 1
            while (i < n - 1 and nums[i] == nums[i + 1]): i += 1
            i += 1
        return res

s = Solution()
print(s.findPairs([3, 1, 4, 1, 5], 2))
# print(s.findPairs([1, 2, 3, 4, 5], 1))
# print(s.findPairs([1, 3, 1, 5, 4], 0))
# print(s.findPairs([1,1,1,1,1], 0))