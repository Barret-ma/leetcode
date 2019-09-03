# Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

# Example 1:

# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
# Example 2:

# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# Example 3:

# Input: ["a==b","b==c","a==c"]
# Output: true
# Example 4:

# Input: ["a==b","b!=c","c==a"]
# Output: false
# Example 5:

# Input: ["c==c","b==d","x!=z"]
# Output: true
 

# Note:

# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='

class UnionFindSet(object):
    def __init__(self, arr):
        self.parents = {}
        self.size = {}
        for i in arr:
            self.parents[i] = i
            self.size[i] = 1
    def union(self, p, q):
        pu = self.find(p)
        qu = self.find(q)
        if pu == qu:
            return
        if self.size[qu] > self.size[pu]:
            self.parents[pu] = qu
            self.size[qu] = self.size[pu] + self.size[qu]
        elif self.size[qu] < self.size[pu]:
            self.parents[qu] = pu
            self.size[pu] = self.size[pu] + self.size[qu]
        else:
            self.parents[pu] = qu
            self.size[qu] = self.size[qu] + 1
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return self.parents[p]

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph = []
        parents = set()
        relationArr = []
        for equation in equations:
            isEqual = False
            if equation.find('==') > -1:
                equation = equation.split('==')
                isEqual = True
            else:
                equation = equation.split('!=')
            parents.add(equation[0])
            parents.add(equation[1])
            if isEqual:
                graph.append([equation[0], equation[1]])
                relationArr.append([equation[0], equation[1], 1])
            else:
                relationArr.append([equation[0], equation[1], -1])

        unionSet = UnionFindSet(list(parents))
        for g in graph:
            unionSet.union(g[0], g[1])

        ans = True
        for item in relationArr:
            root1 = unionSet.find(item[0])
            root2 = unionSet.find(item[1])
            if (item[2] == 1 and root1 != root2) or (item[2] == -1 and root1 == root2):
                return False
        return ans
            



s = Solution()
print(s.equationsPossible(["d!=f","f==e","a==b","a==c"]))