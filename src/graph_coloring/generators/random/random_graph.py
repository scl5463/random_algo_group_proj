import math
import random

from graph_coloring.graph.graph import Graph

# generate a random graph given 
# number of vertices (n), probability of edge (p), and colors (k)
def randomg_npk(n, p, k):
    edgeList = []
    # loop through all possible edges
    for v1 in range(n):
        for v2 in range(n):
            if (v1 < v2):
                # include edge with probability p
                choice = random.randint(0, 1)
                if choice < p:
                    # add edge
                    edgeList.append((v1, v2))

    # create graph
    graph = Graph(range(n), edgeList)

    # color each node with probability k
    for node in range(n):
        color = math.floor(random.random() * k)
        graph.set_vertex_color(node, color)

    return graph