# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from Queue import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = deque([])
        def travel(root, height):
            if len(result) <= height:
                result.appendleft([])
            result[len(result) - height - 1].append(root.val)
            if root.left:
                travel(root.left, height + 1)
            if root.right:
                travel(root.right, height + 1)
        travel(root, 0)
        return result


root = TreeNode(3)
node = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

root.left = node
root.right = node2

node2.left = node3
node2.right = node4

s = Solution()
print s.levelOrderBottom(root)