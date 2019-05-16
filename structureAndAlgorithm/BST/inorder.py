from tree import TreeNode

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

    #         1
    #       /   \
    #      2     3
    #     / \     \
    #    4   5     6
    #       / \
    #      7   8

def inorder(node):
    result = []
    def travel(node, res):
        if not node:
            return
        if node.left:
            travel(node.left, res)
        res.append(node.val)
        if node.right:
            travel(node.right, res)

    travel(root, result)
    return result

def inorderLoop(root):
    stack = []
    result = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            break
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result
    
def morrisInorder(root):
    cur, prev = root, None
    result = []
    while cur:
        if not cur.left:
            result.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
            if not prev.right:
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                result.append(cur.val)
                cur = cur.right
    return result

# print inorder(root)
# print inorderLoop(root)
print(morrisInorder(root))