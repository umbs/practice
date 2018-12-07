import sys

'''
This solution is from one of the Top submissions
'''

# this is needed for passing couple of test cases
sys.setrecursionlimit(100000)

def lca(root, a, b):
    def lcaNode(node, a, b):
        if node in (None, a, b):
            return node

        lt = lcaNode(node.left, a, b)
        rt = lcaNode(node.right, a, b)

        return node if lt and rt else lt or rt

    return lcaNode(root, a, b).data
