# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# maxDepth = 0
class Solution(object):
    maxHeight = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def travel(root, depth):
            if not root:
                # global maxDepth
                # nonlocal maxDepth
                if depth > self.maxHeight:
                    self.maxHeight = depth
                return 0
            # if root.left:
            travel(root.left, depth + 1)

            # if root.right:
            travel(root.right, depth + 1)
        travel(root, 0)
        return self.maxHeight

node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
root = TreeNode(0)

# root.left = node2
# root.right = node3
# node3.left = node4
# node3.right = node5
# node5.left = TreeNode(10)

s = Solution()
print s.maxDepth(root)

