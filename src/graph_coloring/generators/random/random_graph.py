import math
import random

from graph_coloring.graph.graph import Graph

# generate a random graph given 
# number of vertices (n), probability of edge (p), and colors (k)
def randomg_npk(n, p, k):
    vertex_colors = {vertex: None for vertex in range(n)}
    # uniformly color each node one of k colors
    for node in range(n):
        color = math.floor(random.random() * k)
        vertex_colors[node] = color

    edgeList = []
    # loop through all possible edges
    for v1 in range(n):
        for v2 in range(n):
            if (v1 < v2) and vertex_colors[v1] != vertex_colors[v2]:
                # include edge with probability p
                choice = random.randint(0, 1)
                if choice < p:
                    # add edge
                    edgeList.append((v1, v2))

    # create graph
    graph = Graph(range(n), edgeList)

    # set colors
    for node in range(n):
        graph.set_vertex_color(node, vertex_colors[node])

    return graph