class Node:
    def __init__(self, data):
        self.data = data
        self.kids = set()


class Tree:

    def add_edge(self, a, b):
        a.kids.add(b)
        b.kids.add(a)

    # iterative approach
    def dfs_iter(self, root):
        seen, stack = set(), list()
        seen.add(root)
        stack.append(root)

        while stack:
            node = stack.pop()

            # TODO: do something with n

            for a in node.kids.iteritems():
                if a in seen:
                    continue

                seen.add(a)
                stack.append(a)

        return seen


    def dfs_recur(self, root):
        seen = set()
        seen.add(root)
        return self.explore(root, seen)


    def explore(self, node, seen):

        # TODO: do something with node

        for n in node.kids.iteritems():
            if n in seen:
                continue

            seen.add(n)
            self.explore(n, seen)


if __name__ == "__main__":
    tree = Tree()
