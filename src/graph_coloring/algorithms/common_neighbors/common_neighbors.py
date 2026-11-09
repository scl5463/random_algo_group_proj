from graph_coloring.graph.graph import Graph
from graph_coloring.generators.random import random_graph
import matplotlib.pyplot as plt


# return the number of neighbors in common between two vertices
def num_common_neighbors(graph, vertex1, vertex2):
    v1_neighbors = graph.get_neighbors(vertex1)
    v2_neighbors = graph.get_neighbors(vertex2)
    return len(set(v1_neighbors).intersection(set(v2_neighbors)))


# graph histogram of number of neighbors
def graph_neighborshist(graph):
    vals = []
    for vertex1 in graph.vertices:
        for vertex2 in graph.vertices:
            if vertex2 < vertex1:
                vals.append(num_common_neighbors(graph, vertex1, vertex2))
    plt.hist(vals, bins=range(min(vals), max(vals) + 1, 1))
    plt.title('Common neighbors')
    plt.xlabel('Number of neighbors')
    plt.ylabel('frequency')
    plt.show() 
                

# gives 2d visualization of vertices to number of neighbors
def graph_common_neighbors(graph):
    num_verts = len(graph.vertices)
    neighbor_grid = [ [0]*num_verts for i in range(num_verts)]
    
    for vertex1 in graph.vertices:
            for vertex2 in graph.vertices:
                if vertex2 < vertex1:
                    common_neighbors = num_common_neighbors(graph, vertex1, vertex2)
                    neighbor_grid[vertex1][vertex2] = common_neighbors
                    # plt.text(vertex1 - 1, vertex2 - 1, common_neighbors)

    plt.imshow(neighbor_grid, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.xlabel('vertex 1')
    plt.ylabel('vertex 2')
    plt.title('Neighbors of two vertices')
    plt.show()

# return the color of a vertex
def getvertcolor(v, color_to_verts):
    for col, verts in color_to_verts.items():
        if v in verts:
            return col
    return -1

# check if vertices in two classes are combinable
def check_colorable(graph, v1col, v2col, color_to_verts):
    if v1col == v2col:
        return True
    
    c1verts = color_to_verts[v1col]
    c2verts = color_to_verts[v2col]
    
    # check if theres an edge between any vertices
    for vert1 in c1verts:
        for vert2 in c2verts:
            if vert1 in graph.get_neighbors(vert2):
                return False
    return True

def common_neighbors_alg(graph):
    n = len(graph.vertices)
    # first assign each vertex its own color
    color_to_verts = dict()
    for x in range(n):
        color_to_verts[x] = [x]
    # loop through by verts with most common neighbors 
    all_pairs = []
    for x in graph.vertices:
        for y in graph.vertices:
            if x < y:
                all_pairs.append([x, y])
    all_pairs = sorted(all_pairs, key=lambda x:num_common_neighbors(graph, x[0], x[1]), reverse=True)
    for pair in all_pairs:
        # combine
        v1col = getvertcolor(pair[0], color_to_verts)
        v2col = getvertcolor(pair[1], color_to_verts)
        if v1col != v2col and check_colorable(graph, v1col, v2col, color_to_verts):
            color_to_verts[v1col].extend(color_to_verts[v2col])
            del color_to_verts[v2col]

    print(f"colored in {len(color_to_verts.keys())} colors")
    # create colored graph
    colored_graph = Graph(graph.vertices, graph.edges)
    i = 0
    for verts in color_to_verts.values():
        for vert in verts:
            colored_graph.set_vertex_color(vert, i)
        i += 1
    return colored_graph


# new_graph = random_graph.randomg_npk(100, 0.1, 3)
# graph_common_neighbors(new_graph)
# graph_neighborshist(new_graph)
# common_neighbors_alg(new_graph).drawGraph()
