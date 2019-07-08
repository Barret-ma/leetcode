class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def getSubSets(start, out):
            res.append(out)
            for i in range(start, len(nums)):
                getSubSets(i + 1, out + [nums[i]])
        getSubSets(0, [])
        return res

test = Solution()
print test.subsets([1,2,3])

print test.subsets([1])
print test.subsets([])