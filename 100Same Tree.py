# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        resultp = []
        resultq = []
        def travel(root, res):
            if not root:
                return
            res.append(root.val)
            if root.left:
                travel(root.left, res)
            res.append(None)
            if root.right:
                travel(root.right, res)
            res.append(None)
        travel(p, resultp)
        travel(q, resultq)
        for i in range(len(resultp)):
            if resultp[i] != resultq[i]:
                return False
        return True


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(1)
root.left = node2
root.right = node3

root1 = TreeNode(1)
node21 = TreeNode(1)
node31 = TreeNode(2)
root1.left = node21
root1.right = node31

s = Solution()
print s.isSameTree(root, root1)

            