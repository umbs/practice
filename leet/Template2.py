from collections import deque
from typing import List
from pprint import pprint

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeFromList:
    def __init__(self, node: TreeNode, idx=1):
        self.node = node
        self.idx = idx


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        add = 0
        q = deque(root)
        while True:
            lvl = len(q)
            add = 0
            while lvl:
                node = q.pop()
                add += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvl -= 1
        
            if not q:
                break

        return add


def buildTreeLevelOrder(lst: List, idx) -> TreeNode:
    """ Input List is given in level order
    """
    if idx >= len(lst):
        return

    if lst[idx] is None:
        return

    node = TreeNode(lst[idx])
    node.left = buildTreeLevelOrder(lst, 2*idx+1)
    node.right = buildTreeLevelOrder(lst, 2*idx+2)

    return node

def inorderPrint(root: TreeNode) -> None:
    """ Inorder printing """
    if not root:
        return

    inorderPrint(root.left)
    pprint(root.value)
    inorderPrint(root.right)

def levelPrint(root: TreeNode) -> None:


if __name__ == "__main__":
    inp = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
    root = buildTreeLevelOrder(inp, 0)
    import pdb
    pdb.set_trace()
    levelPrint(root)

