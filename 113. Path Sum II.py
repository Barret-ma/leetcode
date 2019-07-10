# Given a binary tree and a sum, find all root-to-leaf
# paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results = []
        self.travel(root, sum, root.val, [root.val], results)
        return results

    def travel(self, root, target, sum, nodes, results):
        if not root.right and not root.left and sum == target:
            results.append(nodes)
            return

        if root.right:
            self.travel(root.right, target, sum + root.right.val,
                        nodes + [root.right.val], results)

        if root.left:
            self.travel(root.left, target, sum + root.left.val,
                        nodes + [root.left.val], results)
