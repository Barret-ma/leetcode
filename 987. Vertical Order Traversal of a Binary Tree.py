# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []

        def travel(root, height):
            if not root.left and not root.right:
                pass
            if root.left:
                travel(root.left, height + 1)
            if root.right:
                travel(root.right, height - 1)