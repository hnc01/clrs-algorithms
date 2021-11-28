from graph import Graph, Vertex
from algorithms import bfs, dfs, topological_sort, strongly_connected_components, print_path
from shortest_path_algorithms import bellman_ford, dag_shortest_paths, dijkstra

'''
    <-- Start: BFS Demo -->
'''


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


'''
    <!-- End: BFS Demo -->
'''

'''
    <-- Start: DFS Demo -->
'''


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


def dfs_demo():
    G = create_dfs_demo_graph()

    dfs(G)

    for vertex in G.V:
        print(str(vertex))


'''
    <!-- End: DFS Demo -->
'''

'''
    <-- Start: Topological Sort Demo -->
'''


def create_topological_sort_demo_graph():
    # create the vertices in the graph
    undershorts = Vertex("undershorts")
    pants = Vertex("pants")
    belt = Vertex("belt")
    shirt = Vertex("shirt")
    tie = Vertex("tie")
    jacket = Vertex("jacket")
    socks = Vertex("socks")
    shoes = Vertex("shoes")
    watch = Vertex("watch")

    G = Graph()

    vertices = [undershorts, pants, belt, shirt, tie, jacket, socks, shoes, watch]

    # add the vertices to the graph
    for i in vertices:
        G.add_vertex(i)

    # create the edges
    G.add_directed_edge(undershorts, pants)
    G.add_directed_edge(undershorts, shoes)
    G.add_directed_edge(pants, shoes)
    G.add_directed_edge(pants, belt)
    G.add_directed_edge(belt, jacket)
    G.add_directed_edge(shirt, belt)
    G.add_directed_edge(shirt, tie)
    G.add_directed_edge(tie, jacket)
    G.add_directed_edge(socks, shoes)

    return G


def topological_sort_demo():
    G = create_topological_sort_demo_graph()

    ordered_vertices = topological_sort(G)

    for vertex in ordered_vertices:
        print(vertex)


'''
    <!-- End: Topological Sort Demo -->
'''

'''
    <-- Start: Strongly Connected Components Demo -->
'''


def create_strongly_connected_components_demo_graph():
    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")
    f = Vertex("f")
    g = Vertex("g")
    h = Vertex("h")

    vertices = [a, b, c, d, e, f, g, h]

    G = Graph()

    for vertex in vertices:
        G.add_vertex(vertex)

    G.add_directed_edge(a, b)
    G.add_directed_edge(b, e)
    G.add_directed_edge(b, f)
    G.add_directed_edge(b, c)
    G.add_directed_edge(c, g)
    G.add_directed_edge(c, d)
    G.add_directed_edge(d, h)
    G.add_directed_edge(d, c)
    G.add_directed_edge(e, a)
    G.add_directed_edge(e, f)
    G.add_directed_edge(f, g)
    G.add_directed_edge(g, f)
    G.add_directed_edge(g, h)
    G.add_directed_edge(h, h)

    return G


def strongly_connected_components_demo():
    G = create_strongly_connected_components_demo_graph()

    strongly_connected_components(G)


'''
    <!-- End: Strongly Connected Components Demo -->
'''

'''
    <-- Start: Bellman Ford Demo -->
'''


def create_bellman_ford_demo_graph():
    G = Graph()

    s = Vertex("s")
    t = Vertex("t")
    y = Vertex("y")
    x = Vertex("x")
    z = Vertex("z")

    vertices = [s, t, y, x, z]

    for vertex in vertices:
        G.add_vertex(vertex)

    G.add_weighted_directed_edge(s, t, 6)
    G.add_weighted_directed_edge(s, y, 7)

    G.add_weighted_directed_edge(t, x, 5)
    G.add_weighted_directed_edge(t, y, 8)
    G.add_weighted_directed_edge(t, z, -4)

    G.add_weighted_directed_edge(y, x, -3)
    G.add_weighted_directed_edge(y, z, 9)

    G.add_weighted_directed_edge(x, t, -2)

    G.add_weighted_directed_edge(z, s, 2)
    G.add_weighted_directed_edge(z, x, 7)

    return (G, s)


def bellman_ford_demo():
    G, s = create_bellman_ford_demo_graph()

    bellman_ford(G, s)

    for vertex in G.V:
        print(vertex)


'''
    <!-- End: Bellman Ford Demo -->
'''

'''
    <-- Start: DAG Shortest Path Demo -->
'''


def create_dag_shortest_path_demo_graph():
    G = Graph()

    r = Vertex('r')
    s = Vertex('s')
    t = Vertex('t')
    x = Vertex('x')
    y = Vertex('y')
    z = Vertex('z')

    vertices = [r, s, t, x, y, z]

    for vertex in vertices:
        G.add_vertex(vertex)

    G.add_weighted_directed_edge(r, s, 5)
    G.add_weighted_directed_edge(r, t, 3)

    G.add_weighted_directed_edge(s, x, 6)
    G.add_weighted_directed_edge(s, t, 2)

    G.add_weighted_directed_edge(t, x, 7)
    G.add_weighted_directed_edge(t, y, 4)
    G.add_weighted_directed_edge(t, z, 2)

    G.add_weighted_directed_edge(x, z, 1)
    G.add_weighted_directed_edge(x, y, -1)

    G.add_weighted_directed_edge(y, z, -2)

    return G, s


def dag_shortest_path_demo():
    G, s = create_dag_shortest_path_demo_graph()

    dag_shortest_paths(G, s)

    for vertex in G.V:
        print(vertex)


'''
    <!-- End: DAG Shortest Path Demo -->
'''

'''
    <-- Start: Dijkstra's Shortest Path Demo -->
'''


def create_dijkstra_shortest_path_demo_graph():
    G = Graph()

    s = Vertex('s')
    t = Vertex('t')
    y = Vertex('y')
    x = Vertex('x')
    z = Vertex('z')

    vertices = [s, t, x, y, z]

    for vertex in vertices:
        G.add_vertex(vertex)

    G.add_weighted_directed_edge(s, t, 10)
    G.add_weighted_directed_edge(s, y, 5)

    G.add_weighted_directed_edge(t, y, 2)
    G.add_weighted_directed_edge(t, x, 1)

    G.add_weighted_directed_edge(y, t, 3)
    G.add_weighted_directed_edge(y, x, 9)
    G.add_weighted_directed_edge(y, z, 2)

    G.add_weighted_directed_edge(x, z, 4)

    G.add_weighted_directed_edge(z, s, 7)
    G.add_weighted_directed_edge(z, x, 6)

    return G, s


def dijkstra_shortest_path_demo():
    G, s = create_dijkstra_shortest_path_demo_graph()

    dijkstra(G, s)

    for vertex in G.V:
        print(vertex)


'''
    <!-- End: Dijkstra's Shortest Path Demo -->
'''


def main():
    dijkstra_shortest_path_demo()


if __name__ == "__main__":
    main()
