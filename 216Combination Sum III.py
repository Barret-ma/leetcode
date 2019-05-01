class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def findDFS(start, total, out):
            if len(out) == k:
                    if total == n:
                        res.append(out)
                        return
                    else:
                        return
            for i in range(start, 10):
                
                if total + i > n:
                    return
                else:
                    findDFS(i + 1, total + i, out + [i])

        findDFS(1, 0, [])
        return res

test = Solution()
# print test.combinationSum3(3, 7)
# print test.combinationSum3(3, 9)
# print test.combinationSum3(2, 7)
print test.combinationSum3(3, 15)