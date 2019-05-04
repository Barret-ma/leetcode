"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        result = []
        def travel(root):
            if not root:
                return
            result.append(root.val)
            if not root.children:
                return
            for node in root.children:
                travel(node)
        travel(root)
        return result
node5 = Node(5, [])
node6 = Node(6, [])
node3 = Node(3, [node5, node6])
node2 = Node(2, [])
node4 = Node(4, [])
root = Node(1, [node3, node2, node4])
s = Solution()
print s.preorder(root)