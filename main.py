import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge('A251', 'B3', weight = 3)
G.add_edge('A252', 'B2', weight = 2)
G.add_edge('A253', 'B2', weight = 2)
G.add_edge('A254', 'B1', weight = 3)
G.add_edge('A255', 'B1', weight = 2)
G.add_edge('A251', 'B4', weight = 2)
G.add_edge('A252', 'B3', weight = 3)
G.add_edge('A253', 'B3', weight = 2)
G.add_edge('A254', 'B2', weight = 2)
G.add_edge('A255', 'B2', weight = 3)
G.add_edge('A251', 'B5', weight = 1)
G.add_edge('A254', 'B3', weight = 4)
G.add_edge('A258', 'B2', weight = 3)
G.add_edge('A260', 'B2', weight = 2)

path = nx.shortest_path(G, 'A251', 'A260', weight = 'weight')
path_edges = zip(path, path[1:])
path_edges = set(path_edges) # add a set() path_edges = set(path_edges)after your zip() to get the shortest path color work
# print(path)

subax1 = plt.subplot()
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = labels, font_size = 10)
nx.draw_networkx_nodes(G, pos, nodelist = path, node_color = 'r')
nx.draw_networkx_edges(G, pos, edgelist = path_edges, edge_color = 'r', width = 2)
plt.savefig("graph.png")