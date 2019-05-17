# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.generateBST(nums, 0, len(nums) - 1)
    def generateBST(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left) / 2
        node = TreeNode(nums[mid])
        node.left = self.generateBST(nums, left, mid - 1)
        node.right = self.generateBST(nums, mid + 1, right)
        return node
    
s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))