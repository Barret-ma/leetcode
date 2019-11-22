# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

#         The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

#         Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

#         In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



#         Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

#         For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

#         -2 (K)	-3	     3
#         -5	   -10	     1
#         10	    30	   -5 (P)


#         Note:

#         The knight's health has no upper bound.
#         Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        if m == 0: return -1
        n = len(dungeon[0])

        dp = [[{'cur': 0, 'total': 0} for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0]['cur'] = dungeon[0][0]
        dp[0][0]['total'] = dungeon[0][0]



        for x in range(1, m):
            cur = dp[x - 1][0]['cur']
            total = dp[x - 1][0]['total']
            dp[x][0]['cur'] = cur + dungeon[x][0]
            dp[x][0]['total'] = min(total, dp[x][0]['cur'])

        for y in range(1, n):
            cur = dp[0][y - 1]['cur']
            total = dp[0][y - 1]['total']
            dp[0][y]['cur'] = cur + dungeon[0][y]
            dp[0][y]['total'] = min(total, dp[0][y]['cur'])

        for i in range(1, m):
            for j in range(1, n):
                rightCur = dp[i][j - 1]['cur']
                rightTotal = dp[i][j - 1]['total']
                upCur = dp[i - 1][j]['cur']
                upTotal = dp[i - 1][j]['total']
                if dp[i][j - 1] + dungeon[i][j] > dp[i - 1][j] + dungeon[i][j]:
                    dp[i][j] = dp[i][j - 1] if dp[i][j - 1] + dungeon[i][j] > 0 else dp[i][j - 1] + dungeon[i][j]
                else:
                    dp[i][j] = dp[i - 1][j] +  dungeon[i][j]
                # minHealth = min(dp[i][j], minHealth)

                # if dp[i][j] < 0:
                #     minHealth = min(minHealth, dp[i][j])
                

        return abs(dp[m - 1][n - 1])


s = Solution()
route = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
s.calculateMinimumHP(route)