def findSingleValueTrees(node):
    result = dict()
    univalCount(node, node.val, 0, result)
    print(result)
    # return len(result)

def univalCount(node, value, count_nodes, result):
    if node is None:
        return

    if node.val == value:
        count_nodes += 1
        result[value] = count_nodes
    else:
        count_nodes = 0
        result.pop(value, None)

    univalCount(node.left, value, count_nodes, result)
    univalCount(node.right, value, count_nodes, result)
