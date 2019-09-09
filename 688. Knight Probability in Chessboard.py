# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

# A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

 



 

# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

# The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 

# Example:

# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.
 

# Note:

# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.


class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # dp = [[0 for i in range(N)] for j in range(N)]
        # dp[r][c] = 1
        # directions = [(1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
        # for k in range(K):
        #     new_dp = [[0 for i in range(N)] for j in range(N)]
        #     for i in range(N):
        #         for j in range(N):
        #             for d in directions:
        #                 x, y = i + d[0], j + d[1]
        #                 if x < 0 or x >= N or y < 0 or y >= N:
        #                     continue
        #                 new_dp[i][j] += dp[x][y]
        #     dp = new_dp
        #     print(dp)

        # return sum(map(sum, dp)) / float(8 ** K)

        dp0 = [[0 for i in range(N)] for j in range(N)]
        dp0[r][c] = 1
        dirs = [(1, 2), (-1, -2), (1, -2), (-1, 2), (2, 1), (-2, -1), (2, -1), (-2, 1)]
        for k in range(K):
            dp1 = [[0 for i in range(N)] for j in range(N)]
            for i in range(N):
                for j in range(N):
                    for m in range(8):
                        y = j + dirs[m][1]
                        x = i + dirs[m][0]
                        if x < 0 or y < 0 or x >= N or y >= N:
                            continue
                        dp1[i][j] = dp1[i][j] + dp0[y][x]
            dp0 = dp1

        total = 0
        for i in range(N):
            for j in range(N):
                total = total + dp0[i][j]
        return float(total) / (8 ** K)

s = Solution()
print(s.knightProbability(3, 2, 0, 0))