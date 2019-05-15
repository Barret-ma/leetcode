# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Example 1:

# Input: [1,3,null,null,2]

#    1
#   /
#  3
#   \
#    2

# Output: [3,1,null,null,2]

#    3
#   /
#  1
#   \
#    2
# Example 2:

# Input: [3,1,4,null,null,2]

#   3
#  / \
# 1   4
#    /
#   2

# Output: [2,1,4,null,null,3]

#   2
#  / \
# 1   4
#    /
#   3
# Follow up:

# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        result = []
        self.travel(root, result)
        print(result)

    def travel(self, root, res):
        if not root:
            res.append(None)
            return
        self.travel(root.left, res)
        res.append(root.val)
        self.travel(root.right, res)

# def createTreeNode(nodeList):
#     root = None
#     for nodeVal in nodeList:
#         root = TreeNode(nodeVal)
        

root = TreeNode(1)
node1 = TreeNode(3)
node2 = TreeNode(2)

root.left = node1
node1.right = node2

s = Solution()
s.recoverTree(root)

# http://www.cnblogs.com/grandyang/p/4297300.html