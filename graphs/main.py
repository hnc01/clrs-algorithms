from graph import Graph, Vertex
from algorithms import bfs, dfs, print_path


def create_bfs_demo_graph():
    # create the vertices in the graph
    r = Vertex("r")
    s = Vertex("s")
    t = Vertex("t")
    u = Vertex("u")
    v = Vertex("v")
    w = Vertex("w")
    x = Vertex("x")
    y = Vertex("y")

    G = Graph()

    vertices = [r, s, t, u, v, w, x, y]

    # add the vertices to the graph
    for i in vertices:
        G.add_vertex(i)

    # create the edges
    G.add_edge(r, s)
    G.add_edge(r, v)
    G.add_edge(s, w)
    G.add_edge(w, t)
    G.add_edge(w, x)
    G.add_edge(x, t)
    G.add_edge(x, u)
    G.add_edge(x, y)
    G.add_edge(t, u)
    G.add_edge(u, y)

    return (G, s, v)


def bfs_demo():
    G, s, v = create_bfs_demo_graph()

    bfs(G, s)

    print("BFS shortest distance results")

    for vertex in G.V:
        print(vertex)

    print("Shortest path between s and v")

    print_path(G, s, v)


def create_dfs_demo_graph():
    # create the vertices in the graph
    u = Vertex("u")
    v = Vertex("v")
    w = Vertex("w")
    x = Vertex("x")
    y = Vertex("y")
    z = Vertex("z")

    G = Graph()

    vertices = [u, v, w, x, y, z]

    # add the vertices to the graph
    for i in vertices:
        G.add_vertex(i)

    # create the edges
    G.add_directed_edge(u, v)
    G.add_directed_edge(u, x)
    G.add_directed_edge(v, y)
    G.add_directed_edge(w, y)
    G.add_directed_edge(w, z)
    G.add_directed_edge(x, v)
    G.add_directed_edge(y, x)
    G.add_directed_edge(z, z)

    return G


def main():
    G = create_dfs_demo_graph()

    dfs(G)

    for vertex in G.V:
        print(str(vertex))


if __name__ == "__main__":
    main()
