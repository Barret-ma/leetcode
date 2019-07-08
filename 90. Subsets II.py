class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def getSubsets(start, out):
            # if nums[start] != nums[start - 1]:
            res.append(out)
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i - 1]:
                    continue
                getSubsets(i + 1, out + [nums[i]])
                
        getSubsets(0, [])
        return res

test = Solution()
print test.subsetsWithDup([4,4,4,1,4])