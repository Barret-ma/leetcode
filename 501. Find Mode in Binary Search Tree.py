# Given a binary search tree (BST) with duplicates, find all the mode(s) 
# (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# For example:
# Given BST [1,null,2,2],

#    1
#     \
#      2
#     /
#    2
 

# return [2].

# Note: If a tree has more than one mode, you can return them in any order.

# Follow up: Could you do that without using any extra space? 
# (Assume that the implicit stack space incurred due to recursion does not count).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution(object):
    cnt = 1
    mx = 0
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    #  Extra Space
    #     if not root:
    #         return []
    #     if not root.left and not root.right:
    #         return [root.val]
    #     result = []
    #     mx = [0]
    #     map = defaultdict(lambda: 0)
    #     self.travel(root, mx, map)
    #     for item in map.items():
    #         (k, v) = item
    #         if v == mx[0]:
    #             result.append(k)
    #     return result

    # def travel(self, root, mx, mp):
    #     if root.left:
    #         self.travel(root.left, mx, mp)
    #     # res.append(root.val)
    #     mx[0] = max(mx[0], mp[root.val] + 1)
    #     mp[root.val] += 1
    #     if root.right:
    #         self.travel(root.right, mx, mp)
        
    # O(1) Space
        if not root:
            return []
        
        result = [[]]
        pre = None
        self.inorder(root, pre, result)
        return result[0]
    def inorder(self, root, pre, res):
        if root.left:
            self.inorder(root.left, pre, res)
        if pre:
            print(pre.val)
            self.cnt = self.cnt + 1 if pre.val == root.val else 1
        if self.cnt >= self.mx:
            if self.cnt > self.mx:
                res[0] = []
            res[0].append(root.val)
            self.mx = self.cnt
        pre = root
        if root.right:
            self.inorder(root.right, pre, res)
                


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(2)

root.right = node1
node1.right = node2

s = Solution()
print(s.findMode(root))
