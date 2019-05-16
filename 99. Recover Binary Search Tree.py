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
        self.morrisInorder(root)

    def morrisInorder(self, root):
        cur, prev = root, None
        first, second, parent = None, None, None

        while cur:
            if not cur.left:
                if parent and parent.val > cur.val:
                    if not first:
                        first = parent
                    second = cur
                parent = cur
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    if parent.val > cur.val:
                        if not first:
                            first = parent
                        second = cur
                    parent = cur
                    cur = cur.right
        first.val, second.val = second.val, first.val   

root = TreeNode(1)
node1 = TreeNode(3)
node2 = TreeNode(2)

root.left = node1
node1.right = node2

s = Solution()
s.recoverTree(root)

# http://www.cnblogs.com/grandyang/p/4297300.html