import cProfile
import pstats
import networkx as nx

GRAPH_NODES = 3000

G = nx.barabasi_albert_graph(GRAPH_NODES, 5)

profiler = cProfile.Profile()

profiler.enable()

nx.betweenness_centrality(G)

profiler.disable()

stats = pstats.Stats(profiler)

stats.sort_stats("cumtime")

stats.print_stats(40)