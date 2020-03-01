# Notes from class on 2/11/2020
# Pseudo code

def bfs(Graph, s):
    s.visited = True
    que.append(s)

    while que:
        p = que.popleft()

        # Do something here

        for n in p.neighbor:
            if not n.visited:
                n.visited = True
                que.append(n)
