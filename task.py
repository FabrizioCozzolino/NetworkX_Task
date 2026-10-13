import math
from collections import deque

import networkx as nx

# Check readme.md for details on each sub-task

def calculate_node_degrees(edges: list) -> dict:
    """Sub-task 1: Calculate the degree of each node in an undirected graph."""
    dict = nx.Graph()

    # In NetworkX i NODI possono essere quasi tutto (purché 'hashable')
    dict.add_node(1)  # Un numero
    dict.add_node("Nodo_A")  # Una stringa
    dict.add_node(math.cos)  # Una funzione!

    # Gli ARCHI collegano i nodi e possono avere attributi arbitrari
    # Se i nodi non esistono, vengono creati automaticamente
    dict.add_edge(1, 2)  # Arco base (peso di default = 1)
    dict.add_edge(2, 3, weight=0.9)  # Specifica di un attributo 'weight'

    # Possiamo aggiungere molti archi contemporaneamente usando liste di tuple
    elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
    dict.add_weighted_edges_from(elist)

    print(f"Nodi nel grafo: {dict.nodes()}")
    print(f"Archi nel grafo: {dict.edges()}\n")

    print(f"Vicini del nodo 2: {dict[2]}")

    return dict
    pass

def find_shortest_path(edges: list, source: str, target: str) -> list:
    """Sub-task 2: Find the shortest path between source and target nodes."""

    class Graph():

        def __init__(self, vertices):
            self.V = vertices
            self.graph = [[0 for column in range(vertices)]
                          for row in range(vertices)]

        def printSolution(self, dist):
            print("Vertex \t Distance from Source")
            for node in range(self.V):
                print(node, "\t\t", dist[node])

        # A utility function to find the vertex with
        # minimum distance value, from the set of vertices
        # not yet included in shortest path tree
        def minDistance(self, dist, sptSet):

            # Initialize minimum distance for next node
            min = 1e7

            # Search not nearest vertex not in the
            # shortest path tree
            for v in range(self.V):
                if dist[v] < min and sptSet[v] == False:
                    min = dist[v]
                    min_index = v

            return min_index

        # Function that implements Dijkstra's single source
        # shortest path algorithm for a graph represented
        # using adjacency matrix representation
        def dijkstra(self, src):

            dist = [1e7] * self.V
            dist[src] = 0
            sptSet = [False] * self.V

            for cout in range(self.V):

                # Pick the minimum distance vertex from
                # the set of vertices not yet processed.
                # u is always equal to src in first iteration
                u = self.minDistance(dist, sptSet)

                # Put the minimum distance vertex in the
                # shortest path tree
                sptSet[u] = True

                # Update dist value of the adjacent vertices
                # of the picked vertex only if the current
                # distance is greater than new distance and
                # the vertex in not in the shortest path tree
                for v in range(self.V):
                    if (self.graph[u][v] > 0 and
                            sptSet[v] == False and
                            dist[v] > dist[u] + self.graph[u][v]):
                        dist[v] = dist[u] + self.graph[u][v]

            self.printSolution(dist)

    # Driver program
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)
    pass

def count_connected_components(edges: list) -> int:
    """Sub-task 3: Count the number of connected components in an undirected graph."""

    def bfs(node, graph, visited):
        queue = deque([node])
        visited.add(node)

        while queue:
            current_node = queue.popleft()
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def count_components(graph):
        visited = set()
        components = 0
        for node in graph:
            if node not in visited:
                bfs(node, graph, visited)
                components += 1
        return components
    pass

def compute_topological_sort(directed_edges: list) -> list:
    """Sub-task 4: Compute a topological ordering of nodes in a DAG."""
    from collections import defaultdict, deque

    class Graph:
        def __init__(self, vertices):
            self.graph = defaultdict(list)
            self.V = vertices

        def addEdge(self, u, v):
            self.graph[u].append(v)

        # Function to perform Kahn's Algorithm
        def topologicalSort(self):
            in_degree = [0] * self.V  # Count of incoming edges for each vertex

            # Calculate in-degree for each vertex
            for u in self.graph:
                for v in self.graph[u]:
                    in_degree[v] += 1

            # Queue for vertices with 0 in-degree
            queue = deque([i for i in range(self.V) if in_degree[i] == 0])
            topo_order = []

            while queue:
                u = queue.popleft()
                topo_order.append(u)

                # Decrease in-degree for adjacent vertices
                for v in self.graph[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

            print(topo_order)

    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    g.topologicalSort()
    pass

def compute_average_clustering(edges: list) -> float:
    """Sub-task 5: Compute the average clustering coefficient of an undirected graph."""
    import networkx as nx

    G = nx.Graph()

    G.add_edges_from([('A', 'B'), ('A', 'K'), ('B', 'K'), ('A', 'C'),
                      ('B', 'C'), ('C', 'F'), ('F', 'G'), ('C', 'E'),
                      ('E', 'F'), ('E', 'D'), ('E', 'H'), ('I', 'J')])

    # returns a Dictionary with clustering value of each node
    print(nx.clustering(G))

    # This returns clustering value of specified node
    print(nx.clustering(G, 'C'))
    pass

def main():
    print("Sub-task 1:", calculate_node_degrees([("A", "B"), ("B", "C"), ("B", "D")]))
    print("Sub-task 2:", find_shortest_path([("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")], "A", "D"))
    print("Sub-task 3:", count_connected_components([("A", "B"), ("B", "C"), ("D", "E")]))
    print("Sub-task 4:", compute_topological_sort([("A", "B"), ("B", "C")]))
    print("Sub-task 5:", compute_average_clustering([("A", "B"), ("B", "C"), ("C", "A")]))

if __name__ == "__main__":
    main()
