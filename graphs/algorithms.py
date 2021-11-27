from graph import Graph, Vertex, WHITE, GREY, BLACK


# a graph instance G
# source vertex s in G
def bfs(G: Graph, s: Vertex):
    for u in G.V:
        # initialize every vertex except for the source vertex
        if u != s:
            u.color = WHITE
            u.d = float("-inf")
            u.parent = None

    # initialize the source vertex
    s.color = GREY
    s.d = 0
    s.parent = None

    # initialize empty list
    Q = []

    # add the source vertex to the queue
    Q.append(s)

    # now we keep iterating over the vertices in the queue until the queue is empty
    while len(Q) != 0:
        # the vertex we need to now explore
        u = Q.pop(0)

        # before exploring the vertex, we first need to add its unvisited neighbors to the queue so they
        # can be explored next
        u_adjacency = G.get_adjacent(u)

        for v in u_adjacency:
            # this guarantees that we don't re-explore discovered or explored vertices
            if v.color == WHITE:
                v.color = GREY
                v.d = u.d + 1
                v.parent = u

                Q.append(v)

        # now that we're not exploring u, we mark it as explored
        u.color = BLACK


def print_path(G: Graph, s: Vertex, v: Vertex):
    if v == s:
        # in this case we reached the source vertex so we print it and exit
        print(s)
    elif v.parent is None:
        # if we reached a node that has no parent (if we're here it also means that v is not the source s)
        # then there's no path from s to v since we couldn't reach s by following the path of v's parents up the tree
        print("no path from s to v")
    else:
        # we're at a node that has a parent but we still didn't reach s so we recurse on the parent and print the current node
        # v after we're done processing its ancestors
        print_path(G, s, v.parent)
        print(v)

time = 0

def dfs(G):
    # we initialize every vertex in G
    for u in G.V:
        u.color = WHITE
        u.parent = None

    # we dfs visit every undiscovered vertex in G
    for u in G.V:
        if u.color == WHITE:
            dfs_visit(G, u)

def dfs_visit(G, u):
    global time

    time = time + 1

    # we are exploring u now so we need to mark it as grey
    u.discovery_time = time
    u.color = GREY

    u_adjacency = G.get_adjacent(u)

    # now discover every edge reachable from u
    for v in u_adjacency:
        if v.color == WHITE:
            # u is v's parent in the DFS tree
            v.parent = u
            dfs_visit(G, v)

    # we're done exploring u
    u.color = BLACK

    time = time + 1

    u.finish_time = time
