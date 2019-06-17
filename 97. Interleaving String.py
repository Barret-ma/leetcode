# coding=UTF-8
# Given s1, s2, s3, find whether s3 is formed by the interleaving 
# of s1 and s2.

# Example 1:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # ls1 = len(s1)
        # ls2 = len(s2)
        # ls3 = len(s3)
        # if ls1 + ls2 != ls3:
        #     return False
        # dp = [[False] * (ls2 + 1) for _ in range(ls1 + 1)]
        # dp[0][0] = True
        # for i in range(1, ls1):
        #     dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        # for j in range(1, ls2):
        #     dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        # for i in range(1, ls1):
        #     for j in range(1, ls2):
        #         dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[j - 1 + i])
        # return dp[ls1][ls2]

        if len(s1)+len(s2)!=len(s3):
            return False
        DP=[[False]*(len(s2)+1) for i in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    DP[i][j]=True
                elif i>0 and DP[i-1][j] and s3[i+j-1]==s1[i-1]:
                    DP[i][j]=True
                elif j>0 and DP[i][j-1] and s3[i+j-1]==s2[j-1]:
                    DP[i][j]=True
                else: #由于DP被初始化为全False，因此，该else语句可以省去
                    DP[i][j]=False

        return DP[len(s1)][len(s2)]


s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))