class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i - 1]
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """ 
        return self.dp[j] if i == 0 else self.dp[j] - self.dp[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
s = NumArray([-2, 0, 3, -5, 2, -1])

print s.sumRange(0,2)
print s.sumRange(2,5)
print s.sumRange(0,5)