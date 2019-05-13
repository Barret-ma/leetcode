class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        sold = 0
        hold = -float('inf')
        rest = 0

        for price in prices:
            pre_price = sold
            hold = max(hold, rest - price)
            rest = max(rest, pre_price)
            sold = hold + price
        return max(rest, sold)
s = Solution()

print s.maxProfit([1,2,3,0,2])