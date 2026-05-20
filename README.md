# Performance Optimization of NetworkX Betweenness Centrality

## Repository

networkx/networkx

## Baseline Workload

The workload benchmarks the `betweenness_centrality` algorithm on a Barabási–Albert graph generated using:

```python
nx.barabasi_albert_graph(3000, 5)