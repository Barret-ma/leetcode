# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        vals = []

        def preorder(root, x, y):
            if not root:
                return
            vals.append((x, y, root.val))
            preorder(root.left, x - 1, y + 1)
            preorder(root.right, x + 1, y + 1)
        preorder(root, 0, 0)
        ans = []
        last_x = -1000
        print(sorted(vals))
        for x, y, val in sorted(vals):
            if x != last_x:
                ans.append([])
                last_x = x
            ans[-1].append(val)
        return ans
# [0,8,1,null,null,3,2,null,4,5,null,null,7,6]


root = TreeNode(0)
root8 = TreeNode(8)
root1 = TreeNode(1)
root3 = TreeNode(3)
root2 = TreeNode(2)
root4 = TreeNode(4)
root5 = TreeNode(5)
root7 = TreeNode(7)
root6 = TreeNode(6)

root.left = root8
root.right = root1
root1.left = root3
root1.right = root2
root3.right = root4
root2.left = root5
root4.right = root7
root5.left = root6

s = Solution()
print(s.verticalTraversal(root))
