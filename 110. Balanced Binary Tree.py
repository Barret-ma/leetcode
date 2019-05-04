# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        

        if not root:
            return True
        if not root.left and not root.right:
            return True
        if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def getDepth(self, root):
            if not root:
                return 0
            return 1 + max(self.getDepth(root.left), self.getDepth(root.right))

# node2 = TreeNode(9)
# node3 = TreeNode(20)
# node4 = TreeNode(15)
# node5 = TreeNode(7)
root = TreeNode(1)
# nodev2 = TreeNode(2)
# nodev3 = TreeNode(3)
# nodev4 = TreeNode(4)
# root.left = nodev2
# root.right = nodev2
# node2.left = node4
# node2.right = node5
# node4.left = TreeNode(4)
# node3.left = node4
# node3.right = node5

s = Solution()
print s.isBalanced(root)