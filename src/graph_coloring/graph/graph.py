# graph class for uniformity in
# graph coloring algorithms and
# random graph creation algos
# will have edges, vertices, and adjacency list, and vertices colors
# add functions here as you work on algos


# class for graph representation
class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices  # list of int or str
        self.edges = edges  # list of tuples (u, v)
        self.adjacency_list = self.create_adjacency_list()
        self.vertex_colors = {vertex: None for vertex in vertices}

    def create_adjacency_list(self):
        # outputs a dict where keys are vertices and
        # values are lists of adjacent vertices
        adjacency_list = {vertex: [] for vertex in self.vertices}
        for edge in self.edges:
            u, v = edge
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)  # Assuming undirected graph
        return adjacency_list

    def set_vertex_color(self, vertex, color):
        if vertex in self.vertex_colors:
            self.vertex_colors[vertex] = color

    def get_vertex_color(self, vertex):
        return self.vertex_colors.get(vertex)

    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])
