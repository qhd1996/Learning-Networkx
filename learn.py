import networkx as nx

oo = float('inf')

# undirected edge
G = nx.Graph()
G.add_node(1) # add node 1
G.add_edge(2,3) #　add node 2,3 and edge (2,3)
print(G.nodes, G.edges, G.number_of_nodes(), G.number_of_edges())

# directed edge
G = nx.DiGraph()
G.add_edge(2,3)
G.add_edge(3,2)
# G = G.to_undirected()  # convert to undirected edge
print(G.edges)

# weighted directed graph
G = nx.DiGraph()
G.add_weighted_edges_from([(0,1,3.0), (1,2,7.5)]) # weight edge (0,1) 3.0, weight edge (1,2) 7.5
print(G.get_edge_data(1,2))  # return the attribute dictionary associated with edge (1,2)

G.add_weighted_edges_from([(2,3,5)], weight='color')
print(G.edges.data())

G.node[1]['size'] = 10
print(G.nodes.data())

import matplotlib.pyplot as plt

g_data = [(1, 2, 6), (1, 3, 1), (1, 4, 5),
          (2, 3, 5),  (2, 5, 3),
          (3, 4, 5), (3, 5, 6), (3, 6, 4), (4, 6, 2),
          (5, 6, 6)]

# minimum spanning tree
g = nx.Graph()
g.add_weighted_edges_from(g_data)
tree = nx.minimum_spanning_tree(g, algorithm='prim')
print(tree.edges(data=True))

# Shorted path
G = nx.path_graph(5)
print(nx.dijkstra_path(G, 0, 4))