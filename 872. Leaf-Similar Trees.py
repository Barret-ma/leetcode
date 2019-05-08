# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 or not root2:
            return False
        leafs1 = []
        leafs2 = []
        def getLeaf(root, l):
            if not root.left and not root.right:
                l.append(root.val)
                return
            if root.left:
                getLeaf(root.left, l)
            if root.right:
                getLeaf(root.right, l)
        getLeaf(root1, leafs1)
        getLeaf(root2, leafs2)
        return leafs1 == leafs2
                
