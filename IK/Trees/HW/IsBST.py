def util(node, less, more):
    if node is None:
        return True
    if node.val <= less or node.val >= more:
        return False

    return util(node.left, less, node.val) and util(node.right, node.val, more)

def  isBST(root):
    return util(root, -1 * sys.maxint, sys.maxint)
