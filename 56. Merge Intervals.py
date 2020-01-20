# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # n = len(intervals)
        if not intervals or not intervals[0]:
            return
        result = []
        n = len(intervals)
        def cmp(x, y):
            if x < y:
                return -1
            else:
                return 1
        intervals.sort(cmp)
        result.append(intervals[0])
        for i in range(1, n):
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])

        return result


s = Solution()
print(s.merge([[1,4], [0, 4]]))