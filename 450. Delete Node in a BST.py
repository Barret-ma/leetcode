# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Example:

# root = [5,3,6,2,4,null,7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

#     5
#    / \
#   4   6
#  /     \
# 2       7

# Another valid answer is [5,2,6,null,4,null,7].

#     5
#    / \
#   2   6
#    \   \
#     4   7

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return
        cur = root
        pre = TreeNode(-1)
        pre.right = cur
        while cur:
            if key > cur.val:
                pre = cur
                cur = cur.right
            elif key < cur.val:
                pre = cur
                cur = cur.left
            else:
                break
        if not cur:
            if pre.val == key:
                cur == None
            return


        left = cur.left
        right = cur.right
        rightPointer = right

        while rightPointer and rightPointer.left:
            rightPointer = rightPointer.left
        if rightPointer:
            rightPointer.left = left
        elif left:
            if pre.val > left.val:
                pre.left = left
            else:
                pre.right = left
        if pre.val == -1:
            return right
        if pre.right and cur.val == pre.right.val:
            pre.right = right
        else:
            pre.left = right
        return root


n2 = TreeNode(2)
n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)
# n7 = TreeNode(7)
n2.right = n3
# n5.left = n3
# n5.right = n6

# n3.right = n4
# n3.left = n2

# n6.right = n7


s = Solution()

s.deleteNode(n2, 2)

        


        