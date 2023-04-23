import networkx as nx
from pytest import fixture

from src.bellmanford import bellman_ford


@fixture
def graph():
    graph = nx.DiGraph()
    graph.add_edge("tst1", "tst2", weight=-1)
    graph.add_edge("tst2", "tst1", weight=-3)
    return graph


def test_bellmanford(graph: nx.DiGraph):
    negative_cycle = bellman_ford(graph, 'tst1')
    assert set(negative_cycle) == {"tst1", "tst2"}
