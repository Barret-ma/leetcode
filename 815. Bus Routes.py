# We have a list of bus routes. Each routes[i] is a bus 
# route that the i-th bus repeats forever. For example if 
# routes[0] = [1, 5, 7], this means that the first bus 
# (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

# We start at bus stop S (initially not on a bus), and 
# we want to go to bus stop T. Travelling by buses only, 
# what is the least number of buses we must take to reach 
# our destination? Return -1 if it is not possible.

# Example:
# Input: 
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation: 
# The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Note:

# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.
from collections import deque, defaultdict
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        res = 0
        stop2bus = defaultdict(lambda: [])
        q = deque([S])
        visited = set()
        for i in range(len(routes)):
            for stop in routes[i]:
                stop2bus[stop].append(i)

        while len(q) > 0:
            res += 1
            for i in range(len(q), 0, -1):
                cur = q.popleft()
                for bus in stop2bus[cur]:
                    if bus in visited:
                        continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == T:
                            return res
                        q.append(stop)

        return -1


s = Solution()
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
