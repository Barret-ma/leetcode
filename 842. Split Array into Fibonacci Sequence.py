# Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

# Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

# Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

# Example 1:

# Input: "123456579"
# Output: [123,456,579]
# Example 2:

# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
# Example 3:

# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
# Example 4:

# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
# Example 5:

# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
# Note:

# 1 <= S.length <= 200
# S contains only digits.

class Solution(object):
    ans = None
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []
        # for i in range(len(S)):
        self.ans = None
        self.dfs(S, [])
        return self.ans if self.ans != None else []

    def dfs(self, num, fib):
        if len(fib) >= 3:
            for n in range(len(fib) - 2):
                if fib[n] + fib[n + 1] != fib[n + 2]:
                    return False
            # result = ''
            # for f in fib:
            #     result = result + str(f)

            # if len(result) == len(origin):
            if len(num) == 0:
                self.ans = fib
                return
        for m in range(0, len(num)):
            if num[0] == '0' and m >= 1:
                break
            else:
                # fib.append(int(num[:m]))
                if len(num[:m+1]) > len(num[m+1:]) and len(num[m + 1:]) != 0:
                    continue
                if int(num[:m + 1]) > 2147483647:
                    continue
                self.dfs(num[m+1:], fib + [int(num[:m+1])])

s = Solution()
print(s.splitIntoFibonacci('11235813'))
print(s.splitIntoFibonacci('112358130'))
print(s.splitIntoFibonacci('0123'))
print(s.splitIntoFibonacci('1101111'))




