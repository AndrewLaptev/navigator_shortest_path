import floorpath as fp

files = [
    "Kronva/graphs/floor_11.txt",
    "Kronva/graphs/floor_12.txt",
    "Kronva/graphs/floor_13.txt",
    "Kronva/graphs/floor_14.txt",
    "Kronva/graphs/floor_21.txt",
    "Kronva/graphs/floor_22.txt",
    "Kronva/graphs/floor_23.txt",
    "Kronva/graphs/connect_floors.txt"
]
floor_graphs = []

for filename in files:
    floor_graphs.append(fp.init_graph(filename))

# print(fp.fl_find_path("A251", "A275"))
fp.show_graph(floor_graphs[7])
