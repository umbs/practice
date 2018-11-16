
def is_present(root, a):
    '''
    tells if a is present in tree rooted at 'root'
    '''
    if root is None:
        return False

    return root.val == a.val or is_present(root.left, a) or is_present(root.right, a)

def lca(root, a, b):
    if root.val == a.val:
        return a
