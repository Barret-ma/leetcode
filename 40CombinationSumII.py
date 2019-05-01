class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def combinationSumDFS(nums, target, start, out, res):
            if target < 0:
                return
            if target == 0:
                res.append(out)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combinationSumDFS(candidates, target - candidates[i], i + 1, out + [candidates[i]], res)

        candidates.sort()
        res = []
        combinationSumDFS(candidates, target, 0, [], res)
        return res
    
test = Solution()
print test.combinationSum2([10,1,2,7,6,1,5], 8)