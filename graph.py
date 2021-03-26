# This file contains the Graph and Vertex classes.

# The vertex represents a node in the graph. Each vertex/node has a value
# to contain and a dictionary of every other vertex that is connected to it
# (representing edges). The key is the adjacent vertex and the value is the
# weight of the edge.
class Vertex:
    def __init__(self, word):
        self.value = word
        self.adjacent_to = {}

    def __str__(self):
        return str(self.value) + ' linked to: ' + str([e for e in self.adjacent_to])

    def add_adjacent(self, adj, weight=1):
        if adj.value in self.adjacent_to.keys():
            self.adjacent_to[adj.value] += 1
        else:
            self.adjacent_to[adj.value] = weight

    def get_links(self):
        return self.adjacent_to.keys()

    def get_value(self):
        return self.value

    def get_weight(self, word):
        return self.adjacent_to[word]

    def get_weights(self):
        return self.adjacent_to.values()


# A graph object represents a series of directed linked vertices. Each edge
# connecting each vertex is weighted (in one direction). A dictionary
# variable for each graph object contains the key, the value of each vertex,
# and the vertex object itself as a value.
class Graph:
    def __init__(self):
        self.graph_vertices = {}
        self.number_of_vertices = 0

    def add_vertex(self, keyword):
        vertex = Vertex(keyword)
        self.graph_vertices[keyword] = vertex
        self.number_of_vertices += 1

    def add_edge(self, fkey, tkey):
        if fkey not in self.graph_vertices:
            self.add_vertex(fkey)
        if tkey not in self.graph_vertices:
            self.add_vertex(tkey)

        self.graph_vertices[fkey].add_adjacent(self.graph_vertices[tkey])

    def get_vertex(self, key):
        if key in self.graph_vertices:
            return self.graph_vertices[key]
        else:
            return None

    def get_vertices(self):
        return self.graph_vertices.keys()

    def __iter__(self):
        return iter(self.graph_vertices.values())

    def __contains__(self, vertex):
        return vertex in self.graph_vertices
