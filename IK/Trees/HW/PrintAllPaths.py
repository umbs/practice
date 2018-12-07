def util(node, path):
    if node is None:
        return

    # Leaf node
    if node.left is None and node.right is None:
        print (path + ' ' + str(node.val)).strip()
        return

    path = path + ' ' + str(node.val)

    if node.left:
        util(node.left, path)
    if node.right:
        util(node.right, path)

def  printAllPaths(root):
    util(root, '')
