# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    mn = float('inf')
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        self.travel(root)
        return self.mn
    def travel(self, root):
        if not root:
            return
        if (root.right and abs(root.val - root.right.val) < self.mn):
            self.mn = abs(root.val - root.right.val)
        elif (root.left and abs(root.val - root.left.val) < self.mn):
            self.mn = abs(root.val - root.left.val)
        return self.travel(root.left) and self.travel(root.right)