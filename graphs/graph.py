WHITE = 0
GREY = 1
BLACK = 2


class Vertex:
    key = None
    d = -1
    parent = None
    color = -1  # 0 for white, 1 for grey and 2 for black
    discovery_time = -1
    finish_time = -1

    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash((self.key))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.key == other.key and self.parent == other.parent

    def __str__(self):
        if self.parent is not None:
            return str({'key': self.key, 'distance': self.d, 'parent': self.parent.key, 'color': self.color,
                        'discover_time': str(self.discovery_time), 'finish_time': str(self.finish_time)})
        else:
            return str({'key': self.key, 'distance': self.d, 'parent': None, 'color': self.color,
                        'discover_time': str(self.discovery_time), 'finish_time': str(self.finish_time)})


class Graph:
    V = None  # list of vertices in Graph
    E = None  # list of edges in Graph

    def __init__(self):
        self.V = set()
        self.E = {}  # maps vertices to the vertices related to them

    def add_vertex(self, u: Vertex):
        if u not in self.V:
            self.V.add(u)

    # we don't define a weight now because we're working with unweighted graph
    def add_edge(self, u: Vertex, v: Vertex):
        if u in self.V and v in self.V:
            if u not in self.E:
                self.E[u] = set()

            if v not in self.E:
                self.E[v] = set()

            # we add both edges because we are working now with an undirected graph
            self.E[u].add(v)
            self.E[v].add(u)

    # adds a directed edge from u to v
    def add_directed_edge(self, u: Vertex, v: Vertex):
        if u in self.V and v in self.V:
            if u not in self.E:
                self.E[u] = set()

            # we add both edges because we are working now with an undirected graph
            self.E[u].add(v)

    # returns list of vertices adjacent to u in the graph
    def get_adjacent(self, u):
        # return the list of vertices adjacent to u
        if u in self.E:
            return list(self.E[u])

        return []

    def get_transpose(self):
        # we create a new graph with same vertices but reversed edges
        G_t = Graph()
        G_t.V = self.V.copy()

        for source_vertex in self.E:
            original_edges = self.E[source_vertex]

            for destination_vertex in original_edges:
                # create the reverse edge in the transpose graph
                G_t.add_directed_edge(destination_vertex, source_vertex)

        return G_t
