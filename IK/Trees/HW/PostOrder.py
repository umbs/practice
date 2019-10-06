class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr


def isLeaf(node):
    return node.left_ptr or node.right_ptr


# Implement postorder traversal in iterative way
def postorderTraversal(root):
    stk = []
    res = []

    if not root:
        return res

    if isLeaf(root):
        return res.append(root.val)

    stk.append(root)

    while stk:
        node = stk.pop()
        res.append(" " + str(node.val))

        if node.left_ptr:
            stk.append(node.left_ptr)
        if node.right_ptr:
            stk.append(node.right_ptr)

    return ''.join(res[::-1])


if __name__ == "__main__":
    t = TreeNode()
