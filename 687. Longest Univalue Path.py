# Given a binary tree, find the length of the longest path where 
# each node in the path has the same value. This path may or may 
# not pass through the root.

# The length of path between two nodes is represented by the number 
# of edges between them.

 

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2

 

# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2

 

# Note: The given binary tree has not more than 10000 nodes. 
# The height of the tree is not more than 1000.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    total = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.maxSame(root)
        return self.total
    def maxSame(self, root):
        if not root:
            return 0
        left = self.maxSame(root.left)
        right = self.maxSame(root.right)

        if root.left and root.val == root.left.val:
            left = left + 1
        else:
            left = 0
        if root.right and root.val == root.right.val:
            right = right + 1
        else:
            right = 0
        self.total = max(self.total, left + right)
        return max(left, right)