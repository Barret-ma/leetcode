# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if not root or (not root.left and not root.right):
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, leftNode, rightNode):
        
        if not leftNode and not rightNode:
            return True
        elif not leftNode or not rightNode:
            return False
        else:
            if not leftNode.left and not leftNode.right and not rightNode.left and not rightNode.right:
                return leftNode.val == rightNode.val
            else:
                return self.isMirror(leftNode.left, rightNode.right) and self.isMirror(leftNode.right, rightNode.left) and leftNode.val == rightNode.val
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
        # if not root:
        #     return True
        # resultLeft = []
        # resultRight = []
        # def travelLeft(root):
        #     if not root:
                
        #         resultLeft.append(None)
        #         return
        #     resultLeft.append(root.val)
        #     # if root.left:
        #     travelLeft(root.left)
            
        #     # if root.right:
        #     travelLeft(root.right)

            
        # def travelRight(root):
        #     if not root:
        #         resultRight.append(None)
        #         return
        #     resultRight.append(root.val)
        #     # if root.right:
        #     travelRight(root.right)
        #     # if root.left:
        #     travelRight(root.left)
        # travelLeft(root.left)
        # travelRight(root.right)
        # # print resultLeft
        # # print resultRight
        # if len(resultLeft) != len(resultRight):
        #     return False
        # for i in range(len(resultLeft)):
        #     if resultLeft[i] != resultRight[i]:
        #         return False
        # return True
            
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(3)
root = TreeNode(1)

# root.left = node2
# root.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6
# node3.right = node7
s = Solution()
print s.isSymmetric(root)
