class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -float('inf')
        curSum = 0
        for i in range(len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            res = max(res, curSum)
        return res

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))