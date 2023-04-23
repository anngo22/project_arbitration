from typing import List
import networkx as nx


def bellman_ford(graph: nx.DiGraph, src) -> List[float]:
    dist = {}
    prev = {}
    vertex_list = _get_vertex_list(graph)
    for cur in vertex_list:
        prev[cur] = ''
        if cur != src:
            dist[cur] = float('inf')
        else:
            dist[src] = 0
    negative_cycle = []

    for i in range(len(vertex_list) - 1):
        for u, v in graph.edges:
            if dist[u] != float('inf') and dist[u] + graph.get_edge_data(u, v)['weight'] < dist[v]:
                dist[v] = dist[u] + graph.get_edge_data(u, v)['weight']
                prev[v] = u

    for u, v in graph.edges:
        if dist[u] != float('inf') and dist[u] + graph.get_edge_data(u, v)['weight'] < dist[v]:
            ver = prev[v]
            for i in range(len(vertex_list) - 1):
                ver = prev[ver]
            negative_cycle.append(ver)
            ver = prev[ver]
            while ver != negative_cycle[0]:
                negative_cycle.append(ver)
                ver = prev[ver]
            break
    return negative_cycle


def _get_vertex_list(graph: nx.DiGraph) -> list:
    return list({item for sublist in graph.edges for item in sublist})
