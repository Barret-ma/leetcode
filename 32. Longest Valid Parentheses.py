# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack = []
        # res = 0
        # start = 0
        # n = len(s)
        # for i in range(n):
        #     if s[i] == '(':
        #         stack.append(i)
        #     elif s[i] == ')':
        #         if len(stack) == 0:
        #             start = i + 1
        #         else:
        #             stack.pop()
        #             if len(stack) == 0:
        #                 res = max(res, i - start + 1)
        #             else:
        #                 res = max(res, i - stack[-1])
        # return res
        res = 0
        n = len(s)
        dp = [0 for _ in range(n + 1)]

        for i in range(n + 1):
            j = i - 2 - dp[i - 1]
            if (s[i - 1] == '(' or j < 0 or s[j] == ')'):
                dp[i] = 0
            else:
                dp[i] = dp[i - 1] + 2 + dp[j]
                res = max(res, dp[i])


        return res

s = Solution()
s.longestValidParentheses('()(())')