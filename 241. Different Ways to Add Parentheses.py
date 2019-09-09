# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

# Example 1:

# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10


# import itertools


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # if input in memo:
        #     return memo[input]
        res = []
        # memo = {}
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }
        
        for i in range(len(input)):
            if input[i] in '+*-':
                left = self.diffWaysToCompute(input[ : i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        res.append(ops[input[i]](l, r))
        if not res: res.append(int(input))
        # memo[input] = res
        return res
        # def ways(s):
        #     ans = []
        #     for i in range(len(s)):
        #         if s[i] in "+-*":          
        #             ans += [ops[s[i]](l, r) for l, r in itertools.product(ways(s[0:i]), ways(s[i+1:]))]
        #     if not ans: ans.append(int(s))
        #     return ans
        # return ways(input)

s = Solution()
print(s.diffWaysToCompute("2*3-4*5"))



