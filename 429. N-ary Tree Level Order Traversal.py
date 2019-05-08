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
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return []
        if not root.children:
            return [[root.val]]
        def travel(root, height):
            if len(result) <= height:
                result.append([])
            result[height].append(root.val)
            for node in root.children:
                travel(node, height + 1)

        travel(root, 0)
        return result

