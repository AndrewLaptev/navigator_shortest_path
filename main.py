import networkx as nx
import matplotlib.pyplot as plt

verts_arcs_map = {}

with open("graph_symbolic.txt", "r") as file:
    for line in file:
        arr_str = line.split()
        verts_arcs_map[arr_str[0]] = arr_str[1:]
file.close()

G = nx.Graph()

for vert in verts_arcs_map:
    for connection in verts_arcs_map[vert]:
        arc_wght = connection.split(',')
        G.add_edge(vert, arc_wght[0], weight = int(arc_wght[1]))


path = nx.shortest_path(G, 'A260', 'A251', weight = 'weight')
path_edges = zip(path, path[1:])
path_edges = set(path_edges) # add a set() path_edges = set(path_edges)after your zip() to get the shortest path color work
print(path)