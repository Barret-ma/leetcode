import math
from decimal import *
class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        used = len(A) * [0]
        self.ans = 0

        def isSquareful(x, y):
            r = math.floor(math.sqrt(x + y))
            return r * r == y + x
        def findDFS(A, cur, used):
            if len(cur) == len(A):
                self.ans += 1
                return
            for i in range(len(A)):
                if used[i]:
                    continue
                if i > 0 and A[i] == A[i - 1] and  not used[i - 1]:
                    continue
                if len(cur) and not isSquareful(cur[len(cur) - 1], A[i]):
                    continue
                used[i] = 1
                findDFS(A, cur + [A[i]], used)
                used[i] = 0

        findDFS(A, [], used)
        return self.ans

test = Solution()
print test.numSquarefulPerms([1,17,8])

print test.numSquarefulPerms([65,44,5,11])

print test.numSquarefulPerms([2,2,2])

# [11,44,5,65]

# def isSquareful(x, y):
#     r = math.floor(math.sqrt(x + y))
#     print r
#     print (r * r - (x + y))
#     return r * r == y + x


# print isSquareful(17, 1)