# There are N rooms and you start in room 0.  Each room has a distinct number 
# in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

# Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is 
# an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

# Initially, all the rooms start locked (except for room 0). 

# You can walk back and forth between rooms freely.

# Return true if and only if you can enter every room.

# Example 1:

# Input: [[1],[2],[3],[]]
# Output: true
# Explanation:  
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we return true.
# Example 2:

# Input: [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can't enter the room with number 2.
# Note:

# 1 <= rooms.length <= 1000
# 0 <= rooms[i].length <= 1000
# The number of keys in all rooms combined is at most 3000.

# class UnionFindSet(object):
#     def __init__(self, n):
#         self.size = [0] * n
#         self.id = [0] * n

#     def find(self, p):
#         if self.id[p] != p:
#             self.id[p] = self.find(self.id[p])
#         return self.id[p]

#     def union(self, p, q):
#         pv = self.find(p)
#         qv = self.find(q)
#         if pv == qv:
#             return
#         if self.size[pv] > self.size[qv]:
#             self.id[q] = pv
#         elif self.size[pv] < self.size[qv]:
#             self.id[p] = qv
#         else:
#             self.id[p] = qv
#             self.size[qv] += 1
from collections import defaultdict
class Solution(object):
    
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms:
            return False
        n = len(rooms)
        
        # for i in range(n):
        visitedMap = defaultdict(lambda: False)
        visitedMap[0] = True
        self.dfs(rooms, rooms[0], visitedMap)
        
        for i in range(n):
            if not visitedMap[i]:
                return False
        return True


    def dfs(self, rooms, keys, map):
        for j in range(len(keys)):
            if map[keys[j]]: continue
            map[keys[j]] = True
            self.dfs(rooms, rooms[keys[j]], map)

s = Solution()
print(s.canVisitAllRooms([[1],[2],[3],[]]))


s1 = Solution()
print(s1.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

s2 = Solution()
print(s2.canVisitAllRooms([[],[1,1],[2,2]]))

s3 = Solution()
print(s3.canVisitAllRooms([[]]))

