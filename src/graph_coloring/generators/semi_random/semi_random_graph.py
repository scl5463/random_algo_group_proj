import random

from graph_coloring.adversaries.adversaries import probabilistic_man, yes_man
from graph_coloring.graph.graph import Graph


def gs_npk(n, p, k, q=0.5):
    """
    semi random graph gen

    n: number vertices
    p: rate of edge reversal
    k: Number of color classes
    q: prob of include edge in graph (default 0.5)
    """
    # setup
    rng = random.Random()
    vertices = list(range(n))
    edges = []

    # partition into k color classes
    colors = {vertex: vertex % k for vertex in vertices}

    # for each pair of vertices ( in different color classes ), adversary decide if pair gets
    # an edge in graph and then chooses to reverse it with
    # probability p
    for u in range(n):
        for v in range(u + 1, n):
            if colors[u] == colors[v]:
                continue
            probabilistic_decision = probabilistic_man(q)
            if rng.random() < p:
                probabilistic_decision = not probabilistic_decision
            if probabilistic_decision:
                edges.append((u, v))

    graph = Graph(vertices, edges)
    for vertex in vertices:
        graph.set_vertex_color(vertex, colors[vertex])
    return graph
