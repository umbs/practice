# Notes from class on 2/11/2020 by Pavan
# Pseudo code


# Recursive approach
def dfs(s):
    s.visited = True

    # Do something here

    for n in s.neighbor:
        if n.visited is False:
            dfs(Graph, n)


# TODO: Iterative approach

# Other options is, have parents or single variable with multiple values
def detect_cycle(s):
    s.visited = True
    s.visiting = True

    for n in s.neighbor:
        if n.visited is False:
            detect_cycle(n)
        elif n.visiting is True:
            return True
    s.visiting = False

    return False


# Color must be same on alternate levels
def bipartite(s):
    s.visited = True
    s.color = 1

    for n in s.neighbor:
        if n.visited is False:
            n.color = 1 - s.color
            bipartite(n)
        elif n.color == s.color:
            return False

    return True
