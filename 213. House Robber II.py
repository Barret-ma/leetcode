class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def robFirstOrLast(l):
            dp = [0] * len(l)
            dp[0] = l[0]
            dp[1] = max(l[0], l[1])
            for i in range(2, len(l)): 
                dp[i] = max(l[i] + dp[i - 2], dp[i - 1])
            return dp[len(l) - 1]
        return max(robFirstOrLast(nums[1:]), robFirstOrLast(nums[:-1]))

s = Solution()
print s.rob([2,3,2])
