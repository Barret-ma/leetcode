# Given a binary tree and a sum, determine if the tree has
# a root-to-leaf path such that adding up all the values along
# the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return
        return self.travel(root, root.val, sum)

    def travel(self, root, sum, target):
        if not root:
            return False
        if not root.left and not root.right:
            return sum == target
        sumRight = 0
        sumLeft = 0
        if root.right:
            sumRight = root.right.val
        if root.left:
            sumLeft = root.left.val
        return self.travel(root.left, sum + sumLeft, target) or self.travel(root.right, sum + sumRight, target)


root5 = TreeNode(5)
root4 = TreeNode(4)
root11 = TreeNode(11)
root7 = TreeNode(7)
root2 = TreeNode(2)

root5.left = root4
root4.left = root11
root11.left = root7
root11.right = root2

s = Solution()
print(s.hasPathSum(root5, 22))
