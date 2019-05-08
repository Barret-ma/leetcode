class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        vector = [0 for _ in range(n)]
        print vector
        vector[0] = 1
        vector[1] = 1
        for i in range(2,n):
            vector[i] = vector[i - 1] + vector[i - 2]
        return vector[n - 1]
s = Solution()
s.climbStairs(4)