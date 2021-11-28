from graph import Graph, Vertex, WHITE, GREY, BLACK
from algorithms import topological_sort
from min_priority_queue import MIN_HEAP


def initialize_single_source(G: Graph, s: Vertex):
    for vertex in G.V:
        vertex.d = float("+inf")
        vertex.parent = None

    s.d = 0


# here w is the weight of edge (u, v)
def relax(u: Vertex, v: Vertex, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.parent = u


# shortest path for directed weighted algorithms with negative weight cycles
def bellman_ford(G: Graph, s: Vertex):
    initialize_single_source(G, s)

    for i in range(1, len(G.V)):
        for source_vertex in G.E:
            for (destination_vertex, weight) in G.E[source_vertex]:
                relax(source_vertex, destination_vertex, weight)

    for source_vertex in G.E:
        for (destination_vertex, weight) in G.E[source_vertex]:
            if destination_vertex.d > source_vertex.d + weight:
                # it means we have a negative weight cycle
                return False

    # we don't have a negative weight cycle
    return True


# shortest path for directed weighted algorithms with negative weight cycles
def dag_shortest_paths(G: Graph, s: Vertex):
    sorted_vertices = topological_sort(G)

    initialize_single_source(G, s)

    for u in sorted_vertices:
        for (v, w) in G.get_adjacent(u):
            relax(u, v, w)


# shortest path for directed weighted graphs with no negative weights (faster than bellman-ford)
def dijkstra(G: Graph, s: Vertex):
    initialize_single_source(G, s)

    S = set()

    Q = MIN_HEAP(list(G.V.copy()))

    while Q.size != 0:
        u = Q.extract_min()

        S.add(u)

        for (v, w) in G.get_adjacent(u):
            relax(u, v, w)
