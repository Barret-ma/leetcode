# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    total = 0
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = root.val
        self.maxTotal(root)
        return self.total
    def maxTotal(self, root):
        if not root:
            return 0

        left = self.maxTotal(root.left)
        right = self.maxTotal(root.right)
        self.total = max(self.total, left + right + root.val)
        return max(left, right) + root.val

root = TreeNode(1)
root2 = TreeNode(2)
root3 = TreeNode(3)

root.left = root2
root.right = root3

s = Solution()
print(s.maxPathSum(root))