from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.kids = set()


class Tree:

    def add_edge(self, a, b):
        a.kids.add(b)
        b.kids.add(a)


    def bfs(self, root):
        que, seen = deque(), set()
        que.append(root)
        seen.add(root)

        while que:
            node = que.popleft()

            # TODO: Do something with node

            for i in node.kids.iteritems():
                if i in seen:
                    continue

                seen.add(i)
                que.append(i)


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

Following is from LeetCode:
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/submissions/
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        q = deque()
        q.append(root)
        level = 0

        while q:
            sz = len(q)
            level += 1
            for i in range(sz):
                node = q.popleft()
                q.extend(node.children)

        return level


if __name__ == "__main__":
    tree = Tree()
