# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


# The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

# Example:

# Input: [2,1,5,6,2,3]
# Output: 10

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # res = 0
        # l = len(heights)
        # if l == 0: return 0
        # for i in range(l):
        #     if i + 1 < l and heights[i] <= heights[i + 1]:
        #         continue
        #     minH = heights[i]
        #     for j in range(i, 0, -1):
        #         minH = min(heights[j], minH)
        #         area = minH * (i - j + 1)
        #         res = max(res, area)
        # return res
        res = 0
        stack = []
        
        heights.append(0)
        l = len(heights)
        i = 0
        while i < l:
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
            else:
                cur = stack.pop()
                res = max(res, heights[cur] * (i if len(stack) == 0 else (i - stack[-1] - 1)))
                i -= 1
            i += 1
        return res

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))

