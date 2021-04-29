r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

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

