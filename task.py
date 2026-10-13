import math

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
    pass

def count_connected_components(edges: list) -> int:
    """Sub-task 3: Count the number of connected components in an undirected graph."""
    pass

def compute_topological_sort(directed_edges: list) -> list:
    """Sub-task 4: Compute a topological ordering of nodes in a DAG."""
    pass

def compute_average_clustering(edges: list) -> float:
    """Sub-task 5: Compute the average clustering coefficient of an undirected graph."""
    pass

def main():
    print("Sub-task 1:", calculate_node_degrees([("A", "B"), ("B", "C"), ("B", "D")]))
    print("Sub-task 2:", find_shortest_path([("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")], "A", "D"))
    print("Sub-task 3:", count_connected_components([("A", "B"), ("B", "C"), ("D", "E")]))
    print("Sub-task 4:", compute_topological_sort([("A", "B"), ("B", "C")]))
    print("Sub-task 5:", compute_average_clustering([("A", "B"), ("B", "C"), ("C", "A")]))

if __name__ == "__main__":
    main()
