# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if s.val == t.val and self.sameStructure(s.left, t.left) and self.sameStructure(s.right, t.right):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def sameStructure(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val == node2.val:
            return self.sameStructure(node1.left, node2.left) and self.sameStructure(node1.right, node2.right)
        else:
            return False

    
        