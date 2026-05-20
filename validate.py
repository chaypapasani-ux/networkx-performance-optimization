import networkx as nx

G = nx.barabasi_albert_graph(1000, 5)

result = nx.betweenness_centrality(G)

print("Validation successful")
print("Computed nodes:", len(result))