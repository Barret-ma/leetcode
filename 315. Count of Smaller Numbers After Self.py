# You are given an integer array nums and you have to return
#  a new counts array. The counts array has the property where 
# counts[i] is the number of smaller elements to the right of nums[i].

# Example:

# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.

class FenwickTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)
    def update(self, i, delta):
        while (i < len(self.sums)):
            self.sums[i] += delta
            i += self.lowbit(i)

    def query(self, i):
        sum = 0
        while i > 0:
            sum += self.sums[i]
            i -= self.lowbit(i)
        return sum

    def lowbit(self, x):
        return x & (-x)

from collections import defaultdict, OrderedDict
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _sortNums = sorted(nums)
        sortedSet = OrderedDict()
        for num in _sortNums:
            sortedSet[num] = 1

        ranks = defaultdict(lambda: 0)
        rank = 0
        for num in sortedSet:
            rank += 1
            ranks[num] = rank
        ans = []
        tree = FenwickTree(len(ranks))
        for i in range(len(nums) - 1, -1, -1):
            ans.append(tree.query(ranks[nums[i]] - 1))
            tree.update(ranks[nums[i]], 1)
        ans.reverse()
        return ans

s = Solution()
print(s.countSmaller([-1, -2]))