import sys

sys.setrecursionlimit(7000)


class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None

def bst_insert(root, val):
    if root is  None:
        return TreeNode(val)
    root_copy = root
    while (1):
        if (val <= root.val and root.left_ptr != None):
            root = root.left_ptr
        elif (val <= root.val):
            root.left_ptr = TreeNode(val)
            return root_copy
        elif (root.right_ptr != None):
            root = root.right_ptr
        else:
            root.right_ptr = TreeNode(val)
            return root_copy
    return root_copy

'''
    For your reference:

    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

def kth_smallest_element(root, k):
    if root.left_ptr:
        kth_smallest_element(root.left_ptr, k)

    k -= 1
    if k == 0:
        return root.val

    if root.right_ptr:
        kth_smallest_element(root.right_ptr, k)


if __name__ == "__main__":
    f = sys.stdout

    N = int(input())

    root = None

    for i in range(0, N):
        data = int(input())
        root = bst_insert(root, data)
    k = int(input())

    ans = kth_smallest_element(root, k)
    f.write(str(ans) + "\n")

    f.close()	
