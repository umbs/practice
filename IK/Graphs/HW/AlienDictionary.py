from collections import defaultdict


def topo(node, graph, visited, stack):
    visited.add(node)
    for neigh in graph[node]:
        if neigh not in visited:
            topo(neigh, graph, visited, stack)

    stack.append(node)


def find_order(words):
    '''
    words: An array of strings
    '''
    graph = defaultdict(list)

    # Build graph. Go over consecutive words, say a,b. Compare chars
    # sequentially in both words until chars mismatch. If mismatch happens at
    # inded j, then a[j] is before b[j] in the dictionary
    for i in range(1, len(words)):
        a, b = words[i-1], words[i]
        j = 0
        while j < (min(len(a), len(b))):
            if a[j] != b[j]:
                break
            j += 1

        if j < min(len(a), len(b)):
            graph[a[j]].append(b[j])

    '''
    for key in graph:
        print(key, graph[key])
    '''

    visited = set()
    stack = list()
    for k in graph:
        if k not in visited:
            topo(k, graph, visited, stack)

    print(stack)


if __name__ == "__main__":
    find_order(["baa", "abcd", "abca", "cab", "cad"])
