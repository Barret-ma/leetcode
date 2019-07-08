class Solution(object):
    def combinationSum(self, candidates, target):
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
                combinationSumDFS(candidates, target - candidates[i], i, out + [candidates[i]], res)

        candidates.sort()
        res = []
        combinationSumDFS(candidates, target, 0, [], res)
        return res
        
            



            

            


test = Solution()

print test.combinationSum([1, 2,3,3,6,7], 5)