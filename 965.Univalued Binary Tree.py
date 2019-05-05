# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    val = None
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.val = root.val
        return self.travel(root)
    def travel(self, root):
        if not root:
            return True
        if self.val != root.val:
            return False
        if not root.left and not root.right:
            return True

        return self.travel(root.left) and self.travel(root.right)
            
        
root = TreeNode(9)
node1 = TreeNode(9)
node2 = TreeNode(6)
node3 = TreeNode(9)
node4 = TreeNode(9)
# node5 = TreeNode(1)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
# node2.right = node5

s = Solution()
print s.isUnivalTree(root)