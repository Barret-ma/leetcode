# A chess knight can move as indicated in the chess diagram below:

#  .           

 

# This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

# Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

# How many distinct numbers can you dial in this manner?

# Since the answer may be large, output the answer modulo 10^9 + 7.

 

# Example 1:

# Input: 1
# Output: 10
# Example 2:

# Input: 2
# Output: 20
# Example 3:

# Input: 3
# Output: 46
 

# Note:

# 1 <= N <= 5000

class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        # dp = [[1 for _ in range(3)] for n in range(4)]
        # dirs = [(1, 2), (2, 1), (-1, 2), (2, -1), (-1, -2), (-2, -1), (-2, 1), (1, -2)]
        # dp[3][0] = dp[3][2] = 0
        # for j in range(1, N):
        #     temp = [[0 for _ in range(3)] for n in range(4)]
        #     for i in range(4):
        #         for l in range(3):
        #             if i == 3 and l != 1:
        #                 continue
        #             for dir in dirs:
        #                 x = l + dir[0]
        #                 y = i + dir[1]
        #                 if x < 0 or y < 0 or y >= 4 or x >= 3:
        #                     continue
        #                 temp[i][l] = (temp[i][l] + dp[y][x]) % (10 ** 9 + 7)
        #     dp = temp
        # ans = 0
        # for i in range(4):
        #     for j in range(3):
        #         ans = (ans + dp[i][j]) % (10 ** 9 + 7)
        # return ans
        d = {0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4]}
        dp = [[0]*10 for _ in range(N)]
        mod = 10**9 + 7
        for i in range(10): dp[0][i] = 1
        
        for i in range(1, N):
            for j in range(10):
                for nex in d[j]:
                    dp[i][j] += dp[i-1][nex]
                dp[i][j] %= mod
        print(dp)
        return sum(dp[N-1]) % mod
        


s = Solution()
s.knightDialer(2)
