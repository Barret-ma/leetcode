# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note: 
# You may assume k is always valid, 1 <= k <= BST's total elements.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
   k = None
   def kthSmallest(self, root, k):
      """
      :type root: TreeNode
      :type k: int
      :rtype: int
      """
      if not root:
         return
   #      result = []
   #      self.travel(root, result)
   #      return result[k - 1]
   #  def travel(self, root, list):
   #      if root.left:
   #          self.travel(root.left, list)
   #      list.append(root.val)
   #      if root.right:
   #          self.travel(root.right, list)
      self.k = k
      return self.travel(root)
   def travel(self, root):
      if not root:
         return -1
      val = self.travel(root.left)
      if self.k == 0: return val
      self.k -= 1
      if self.k == 0: return root.val
      return self.travel(root.right)

root = TreeNode(3)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(4)

root.left = node1
root.right = node3
node1.right = node2

s = Solution()
print(s.kthSmallest(root, 1))