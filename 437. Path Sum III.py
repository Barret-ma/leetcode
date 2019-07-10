# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf,
# but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the
# range -1,000,000 to 1,000,000.

# Example:

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    count = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return
        self.count = 0
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            self.travel(node, sum, node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return self.count

    def travel(self, root, target, sum):
        if not root:
            return
        if sum == target:
            self.count += 1
            # return
        if root.left:
            self.travel(root.left, target, sum + root.left.val)
        if root.right:
            self.travel(root.right, target, sum + root.right.val)


root = TreeNode(1)
root_2_1 = TreeNode(-2)
root_3 = TreeNode(-3)
root1 = TreeNode(1)
root3 = TreeNode(3)
root_2_2 = TreeNode(-2)
root_1 = TreeNode(-1)
# [1,-2,-3,1,3,-2,null,-1]

root.left = root_2_1
root.right = root_3
root_2_1.left = root1
root_2_1.right = root3
root_3.left = root_2_2


s = Solution()
print(s.pathSum(root, -1))
