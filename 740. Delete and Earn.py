class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        numsCp = [0] * (max(nums) + 1)
        for num in nums:
            numsCp[num] += num
        print(numsCp)
        return self.rob(numsCp)

    def rob(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[len(nums) - 1]
s = Solution()

# [3, 4, 2] 6
# print(s.deleteAndEarn([3, 4, 2]))

# [2, 2, 3, 3, 3, 4] 9
# print(s.deleteAndEarn([2, 2, 3, 3, 3, 4]))

print (s.deleteAndEarn([1]))