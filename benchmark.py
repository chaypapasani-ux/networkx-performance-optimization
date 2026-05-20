import time
import statistics
import networkx as nx

N_WARMUP = 2
N_RUNS = 7

GRAPH_NODES = 3000

def workload():
    G = nx.barabasi_albert_graph(GRAPH_NODES, 5)
    return nx.betweenness_centrality(G)

times = []

print("Warmup runs")

for _ in range(N_WARMUP):
    workload()

print("\nMeasured runs")

for i in range(N_RUNS):
    start = time.perf_counter()

    workload()

    end = time.perf_counter()

    elapsed = end - start
    times.append(elapsed)

    print(f"Run {i+1}: {elapsed:.2f} seconds")

median = statistics.median(times)

quartiles = statistics.quantiles(times, n=4)
iqr = quartiles[2] - quartiles[0]

print("\nMedian:", round(median, 2))
print("IQR:", round(iqr, 2))