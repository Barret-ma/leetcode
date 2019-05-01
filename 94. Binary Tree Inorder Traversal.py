# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def inorder(root, res):
            if not root:
                return
            # before
            # res.append(root.val)
            if root.left:
                inorder(root.left, res)
            # inorder
            # res.append(root.val)
            if root.right:
                inorder(root.right, res)
            # postorder 
            # res.append(root.val)
        inorder(root, result)
        return result

root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
n5.left = n7
n5.right = n8

s = Solution()
print s.inorderTraversal(root)