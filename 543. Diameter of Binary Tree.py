# Given a binary tree, you need to compute the length of the
# diameter of the tree. The diameter of a binary tree is the
# length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    res = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.maxDepth(root)
        return self.res

    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        self.res = max(self.res, left + right)
        return max(left, right) + 1


root1 = TreeNode(1)
root2 = TreeNode(2)
root3 = TreeNode(3)
root4 = TreeNode(4)
root5 = TreeNode(5)
root6 = TreeNode(6)

root1.left = root2
root2.left = root3
root2.right = root4
root3.left = root5
root4.right = root6

s = Solution()
print(s.diameterOfBinaryTree(root1))
