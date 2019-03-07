def inOrder(node, nums):
    if node is None:
        return

    inOrder(node.left, nums)
    nums.append(node.data)
    inOrder(node.right, nums)


def merge(a, b, c):
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c.extend(a[i:])
    else:
        c.extend(b[j:])


def buildBST(arr, l, r):
    if l > r:
        return None

    mid = l + (r-l)/2
    n = Node(arr[mid])
    n.left = buildBST(arr, l, mid-1)
    n.right = buildBST(arr, mid+1, r)

    return n


def mergeTwoBSTs(root1, root2):
    a, b, c = list(), list(), list()
    inOrder(root1, a)
    inOrder(root2, b)
    merge(a, b, c)
    return buildBST(c, 0, len(c)-1)
