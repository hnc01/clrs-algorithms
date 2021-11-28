from graph import Graph, Vertex, WHITE, GREY, BLACK


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
