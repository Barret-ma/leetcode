# Given a binary tree containing digits from 0-9 only, each root-to-leaf
# path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# Note: A leaf is a node with no children.

# Example:

# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:

# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.dfs(root, '', res)
        total = 0
        for item in res:
            total += int(item)
        return total

    def dfs(self, root, lres, res):
        if not root:
            return 0
        if root.right:
            self.dfs(root.right, lres + str(root.val), res)
        if root.left:
            self.dfs(root.left, lres + str(root.val), res)
        if not root.right and not root.left:
            res.append(lres + str(root.val))
            return


root = TreeNode(4)
left = TreeNode(9)
right = TreeNode(0)
root4 = TreeNode(5)
root5 = TreeNode(1)

root.left = left
root.right = right

left.left = root4
left.right = root5

s = Solution()
print(s.sumNumbers(root))
