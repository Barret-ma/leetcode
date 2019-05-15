# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        result = []
        self.travel(root, result)
        mn = float('inf')
        for i in range(1, len(result)):
            if result[i] - result[i - 1] < mn:
                mn = result[i] - result[i - 1]
        return mn
    def travel(self, root, res):
        if root.left:
            self.travel(root.left, res)
        res.append(root.val)
        if root.right:
            self.travel(root.right, res)

s = Solution()

root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(4)

root.right = right
right.left = left

s.getMinimumDifference(root)
