class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        buy = float('inf')
        for price in prices:
            buy = min(buy, price)
            res = max(res, price - buy)
        return res

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
