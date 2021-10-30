# import matplotlib.pyplot as plt


# pos = nx.spring_layout(G)
# nx.draw_networkx(G, pos)
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels = labels, font_size = 7)
# nx.draw_networkx_nodes(G, pos, nodelist = path, node_color = 'r', node_size = 100)
# nx.draw_networkx_edges(G, pos, edgelist = path_edges, edge_color = 'r')
# nx.draw(G, with_labels=True, font_weight = "bold", node_size = 100)

# pos = nx.circular_layout(G)

# colors = nx.get_edge_attributes(G,'color').values()
# weights = nx.get_edge_attributes(G,'weight').values()

# nx.draw(G, pos, edge_color=colors, width=list(weights))

# plt.savefig("graph.png")