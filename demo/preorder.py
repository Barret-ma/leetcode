
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Create a tree
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

def preorder(root):
    result = []
    def travel(node):
        if not node:
            return
        result.append(node.val)
        if node.left:
            travel(node.left)
        if node.right:
            travel(node.right)
    travel(root)
    return result

def preorderLoop(root):
    stack = []
    result = []
    while True:
        while root:
            result.append(root.val)
            stack.append(root)
            root = root.left
        if not stack:
            break
        root = stack.pop()
        root = root.right
    return result

# print preorder(root)
print preorderLoop(root)
