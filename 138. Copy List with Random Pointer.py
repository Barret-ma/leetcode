# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

 

# Example 1:



# Input:
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

# Note:

# You must return the copy of the given head as a reference to the cloned list.


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        headCopy = Node(head.val, None, None)
        m = {head: headCopy}
        self.dfs(head, m)
        return headCopy
    def dfs(self, node, dic):
        if node.next not in dic and node.next != None:
            nodeCopy = Node(node.next.val, None, None)
            dic[node.next] = nodeCopy
            dic[node].next = nodeCopy
            self.dfs(node.next, dic)
        else:
            dic[node].next = None if node.next == None else dic[node.next]

        if node.random not in dic and node.random != None:
            randomCopy = Node(node.random.val, None, None)
            dic[node.random] = randomCopy
            dic[node].random = randomCopy
            self.dfs(node.random, dic)
        else:
            dic[node].random = None if node.random == None else dic[node.random]
