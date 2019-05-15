# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true

# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    rootVal = 0
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.travel(root, -float('inf'), float('inf'))

    def travel(self, root, mn, mx):
        if not root:
            return True
        
        if (root.val <= mn) or (root.val >= mx):
            return False
        return self.travel(root.left, mn, root.val) and self.travel(root.right, root.val, mx)
        
    
root = TreeNode(10)
left = TreeNode(5)
right = TreeNode(15)

node = TreeNode(6)
node2 = TreeNode(20)

root.left = left
root.right = right
right.left = node
node.right = node2

s = Solution()
print(s.isValidBST(root))