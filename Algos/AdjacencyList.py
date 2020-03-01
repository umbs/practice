class Graph:

    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adj_list = [[] for _ in range(num_of_vertices)]

    def add_edge(self, start, end, bidir=True):
        self.adj_list[start].append(end)
        if bidir:
            self.adj_list[end].append(start)

    def has_eulerian_cycle(self):
        # For a graph to have Eulerian cycle, all it's vertices must have even
        # number of edges

        for v in self.adj_list:
            if len(v) % 2 == 1:
                return False

        return True


if __name__ == "__main__":
    g = Graph(10)
