# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        resultList = []
        equationsMap = defaultdict(lambda: defaultdict())

        for i in range(len(equations)):
            equation = equations[i]

            equationsMap[equation[0]][equation[1]] = values[i]

            equationsMap[equation[1]][equation[0]] = 1.0 / values[i]

        for query in queries:
            if query[0] not in equationsMap or query[1] not in equationsMap:
                resultList.append(-1.0)
            else:
                visited = set()
                resultList.append(self.dfs(query, equationsMap, visited))
        return resultList
    def dfs(self, q, m, visited):
        if (q[0] == q[1]): return 1.0
        visited.add(q[0])
        if q[1] in m[q[0]]:
            return m[q[0]][q[1]]
        else:
            for nq in m[q[0]]:
                if nq in visited:
                    continue
                d = self.dfs([nq, q[1]], m, visited)
                if d > 0:
                    return d * m[q[0]][nq]
        return -1.0


s = Solution()
s.calcEquation(
    [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
    [3.0, 4.0, 5.0, 6.0],
    [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
)