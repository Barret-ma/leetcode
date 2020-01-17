from tree import TreeNode

    #         1
    #       /   \
    #      2     3
    #     / \     \
    #    4   5     6
    #       / \
    #      7   8

rootTest = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
rootTest.left = n2
rootTest.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
n5.left = n7
n5.right = n8

def postorder(root):
    result = []

    def dfs(node, res):
        if not node:
            return
        if root.left:
            dfs(node.left, res)
        if root.right:
            dfs(node.right, res)
        res.append(root.val)
    dfs(root, result)
    return result


def postorderLoop(root):
    result = []
    stack = []
    cur = root
    last = None
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack[-1]
        if not cur.right or cur.right == last:
            result.append(cur.val)
            stack.pop()
            last = cur
            cur = None
        else:
            cur = cur.right
    print(result)
    return result

postorderLoop(rootTest)