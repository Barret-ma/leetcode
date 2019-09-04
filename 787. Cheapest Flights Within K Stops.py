# There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
# Note:

# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
from collections import defaultdict
class Solution(object):
    total = float('inf')
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        self.total = float('inf')
        pathMap = defaultdict(lambda: [])
        for city in flights:
            pathMap[city[0]].append((city[1], city[2]))  # next stop, cost
        # total = float('inf')
        for city in flights:
            if city[0] == src:
                visited = {city[0]: True}
                self.dfs(src, dst, K, pathMap, 0, 0, visited)
        return self.total if self.total != float('inf') else -1
    def dfs(self, src, dst, K, pathMap, stops, total, visited):
        
        nextStop = pathMap[src]
        for cur in nextStop:
            if cur[0] == dst and K >= stops:
                self.total = min(total + cur[1], self.total)
        if stops > K:
            return -1
        
        for n in nextStop:
            if n[0] not in visited:
                visited[n[0]] = True
                self.dfs(n[0], dst, K, pathMap, stops + 1, total + n[1], visited)
                del visited[n[0]]


s = Solution()
print(s.findCheapestPrice(10,
[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],
6,
0,
7))