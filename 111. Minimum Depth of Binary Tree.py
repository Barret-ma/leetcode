# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    minHeight = float('inf')
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def travel(root, height):
            if not root.left and not root.right:
                if self.minHeight > height:
                    self.minHeight = height 
                return
            if root.left:    
                travel(root.left, height + 1)
            if root.right:
                travel(root.right, height + 1)
        travel(root, 1)
        return self.minHeight

node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
root = TreeNode(3)

root.left = node2
# root.right = node3
# node3.left = node4
# node3.right = node5

s = Solution()
print s.minDepth(root)