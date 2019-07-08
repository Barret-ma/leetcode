# Given a binary tree, return the vertical order traversal of its nodes values.

# For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values 
# of the nodes in order from top to bottom (decreasing Y coordinates).

# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

# Example 1:



# Input: [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: 
# Without loss of generality, we can assume the root node is at position (0, 0):
# Then, the node with value 9 occurs at position (-1, -1);
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
# The node with value 20 occurs at position (1, -1);
# The node with value 7 occurs at position (2, -2).
# Example 2:



# Input: [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: 
# The node with value 5 and the node with value 6 have the same position according to the given scheme.
# However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

# Note:

# The tree will have between 1 and 1000 nodes.
# Each node's value will be between 0 and 1000.



# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    min = 0
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
