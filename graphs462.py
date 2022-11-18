class Graph:
    def __init__(self, dicts=None):
        if dicts is None:
            dicts = {}
        self.graph = dicts

    # Add a vertices to the graph
    def add_vertex(self, data):
        if data not in self.graph:  # if it doesnt already exist
            self.graph[data] = []  # add the data with an empty value

    # Add a edge to the graph
    def add_edges(self, data):
        data = set(data)
        v1, v2 = tuple(data)
        for x, y in [(v1, v2), (v2, v1)]:
            if x in self.graph:
                self.graph[x].add(y)
            else:
                self.graph[x] = y

    # generate all edges
    # helper function to generate all the edge tuples of the graph
    def generate_edge(self):
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                if {neighbor, node} not in edges:
                    edges.append({node, neighbor})
        return edges

    # returns all the generated edges in the graph
    def get_edges(self):
        return self.generate_edge()

    # function to return the edges at a given vertx
    def edge_at_node(self, node):
        return self.graph[node]

    # generate all vertix
    def get_vertices(self):
        return set(self.graph.keys())

    # calculate isolated nodes in the graph
    def isolated_nodes(self):
        nodes = []
        for vertex in self.graph:
            # print(nodes, vertex)
            if not self.graph[vertex]:
                nodes += [vertex]
        return nodes  # returns a list of isolated nodes.

    # find a path between a start and end vertex
    def find_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        for node in self.graph[start]:
            if node not in path:
                extended_path = self.find_path(node, end, path)
                if extended_path:
                    return extended_path
        return None

    # find all paths
    # The algorithm uses an important technique called backtracking:
    # it tries each possibility in turn until it finds a solution.
    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:  # between a start and end vertex
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                extended_paths = self.find_all_paths(node, end, path)
                for i in extended_paths:
                    paths.append(i)
        return paths

    # check if a graph is connected
    def is_connected(self, encountered=None, start=None):
        # determines if the graph is connected
        if encountered is None:
            encountered = set()
        vertices = list(self.graph.keys())  # "list" necessary in Python 3
        if not start:
            # choose a vertex from graph as a starting point
            start = vertices[0]
        encountered.add(start)
        if len(encountered) != len(vertices):
            # If A is equal to the set of nodes of G, the graph is connected;
            for v in self.graph[start]:
                if v not in encountered:
                    if self.is_connected(encountered, v):
                        return True
        else:
            return True
        return False

    # dfs
    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()

        visited.add(node)
        print(node, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)  # recurse for all vertices

    # bfs
    def bfs(self, node):
        visited = []  # value of visited nodes
        queue = []  # queue of current nodes
        visited.append(node)
        queue.append(node)  # adding to the lists

        while queue:  # Creating loop to visit each node
            m = queue.pop(0)  # remove and print node as it's visited
            print(m, end=" ")

            for neighbour in self.graph[m]:  # loop to check nodes not visited
                if neighbour not in visited:  # and append into the visited/queue list
                    visited.append(neighbour)
                    queue.append(neighbour)

    def dijkstras(self):
        pass

    def kruskals(self):
        pass

    def prims(self):
        pass

    # functions used to help print and iterate over the class objects
    def __iter__(self):
        self.iterate = iter(self.graph)
        return self.iterate

    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self.iterate)

    def __str__(self):
        val = "vertices: "
        for k in self.graph:
            val += str(k) + " "
        val += "\nedges: "
        for edge in self.generate_edge():
            val += str(edge) + " "
        return val

    def __getitem__(self, item):
        print(item)


# supplementary graphs
graph = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
graph2 = {
    "a": ['b', 'c'],
    "b": ['c', 'd'],
    "c": ['d'],
    "d": ['c'],
    "e": ['f'],
    "f": []
}
graph3 = {
    "a": ["d", "f"],
    "b": ["c", "b"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"],
    "z": []
}
gg4 = {
    0: [2, 5, 7],
    1: [7],
    2: [0, 6],
    3: [5, 4],
    4: [3, 6, 7],
    5: [3, 4, 0],
    6: [2, 4],
    7: [0, 1, 4]
}

# creating graph class objects
g = Graph(graph)
g2 = Graph(graph2)
g3 = Graph(graph3)
g4 = Graph(gg4)
# testing the class functions

print("\nGraph 4")
for i in g4:
    print(f"Edges of {i}: ", g4.edge_at_node(i))

print("\nGraph 3")
for vertice in g3:
    print(f"Edges of {vertice}: ", g3.edge_at_node(vertice))

print("Isolated node of graph 3: ", g3.isolated_nodes())
print("Isolated node of graph 4: ", g4.isolated_nodes())

print("\nG3 Path of a,to e:", g3.find_path('a', 'e'))
path = g4.find_all_paths(0, 7)
print("\nG4 ALL Paths to 0,to 7:", path)

print("\nIs G3 Connected?:", g3.is_connected())
print("\nIs G4 Connected?:", g4.is_connected())

print("\nBFS Of G4: ")
g4.bfs(7)

print("\nDFS Of G4: ")
g4.dfs(7)


