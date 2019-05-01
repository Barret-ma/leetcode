class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def combineDFS(start, out):
            if len(out) == k:
                res.append(out)
                return
            for i in range(start, n + 1):
                if i >= start:
                    combineDFS(i + 1, out + [i])
        combineDFS(1, [])
        return res


test = Solution()
print test.combine(4, 2)

print test.combine(3, 3)

print test.combine(1, 1)
