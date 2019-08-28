# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites


class Solution(object):
    _graph = None
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self._graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            self._graph[p[0]].append(p[1])

        v = [0] * numCourses
        for i in range(numCourses):
            if(self.dfs(i, v)): return False
        return True

    def dfs(self, cur, v):
        if v[cur] == 1:
            return True
        if v[cur] == 2:
            return False
        v[cur] = 1
        for t in self._graph[cur]:
            if(self.dfs(t, v)): return True
        v[cur] = 2
        return False