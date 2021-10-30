import networkx as nx

G = nx.Graph()
verts_arcs_map = {}

def init_graph(filename):
    """Initial undirect weighted graph from file
    Parameters
    ----------
    `filename` : text file with strings vertex -> arcs, weight
        Format file: `Vertex1 Vertex2,weight1 Vertex3,weight2...`
        It is mean Vertex1 connect with Vertex2 with weight,
        also Vertex1 connect with Vertex3 with weight2...
    """
    with open(filename, "r") as file:
        for line in file:
            arr_str = line.split()
            verts_arcs_map[arr_str[0]] = arr_str[1:]
    file.close()
    for vert in verts_arcs_map:
        for connection in verts_arcs_map[vert]:
            arc_wght = connection.split(',')
            G.add_edge(vert, arc_wght[0], weight = int(arc_wght[1]))

def fl_find_path(src, dst):
    """Find shortest path between `src` and `dst` on floor
    Parameters
    ----------
    `src` and `dst`: name of cabinet on floor (example: A251)
    """
    path = nx.shortest_path(G, src, dst, weight = 'weight')
    path_edges = zip(path, path[1:])
    path_edges = set(path_edges) # add a set() path_edges = set(path_edges)after your zip() to get the shortest path color work
    return path