# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
#              course 0. So the correct course order is [0,1] .
# Example 2:

# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


class Solution(object):
    _graph = None
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self._graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            self._graph[pre[0]].append(pre[1])
        
        # 0 == unknown  1 == visiting  2 == visited
        v = [0] * numCourses
        orderList = []
        for i in range(numCourses):
            if self.dfs(i, v, orderList):
                return []
        return orderList

    def dfs(self, cur, v, list):
        if v[cur] == 1:
            return True
        if v[cur] == 2:
            return False

        v[cur] = 1
        for p in self._graph[cur]:
            if self.dfs(p, v, list): return True
        v[cur] = 2
        list.append(cur)
        return False




