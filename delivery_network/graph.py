class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        self.nb_edges += 1

        if node1 in self.graph.keys():
            self.graph[node1].append((node2, power_min, dist))
            
        else:
            key, value = node1, (node2, power_min, dist)
            self.graph[key] = [value]
            
        if node2 in self.graph.keys():
            self.graph[node2].append((node1, power_min, dist))
        else:
            key, value = node2, (node1, power_min, dist)
            self.graph[key] = [value]
            
        return self.graph

    def get_path_with_power(self, src, dest, power):
        raise NotImplementedError
    
    def connected_components(self):
        liste_composantes = []
        visited_node = {node : False for node in self.nodes}

        def parcours_profondeur(node):
            composante = [node]
            for voisin in self.graph[node]:
                voisin = voisin[0]
                if not visited_node[voisin]:
                    visited_node[voisin] = True
                    composante += parcours_profondeur(voisin)
            return composante
        for node in self.nodes:
            if not visited_node[node]:
                liste_composantes.append(parcours_profondeur(node))
        return liste_composantes
        
    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        raise NotImplementedError


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename) as file:
        ligne1=file.readline().split()
        n=int(ligne1[0])
        m=int(ligne1[1])
        nodes = [i for i in range(1, n+1)]
        G=Graph(nodes)
        for i in range(m):
            lignei=file.readline().split()
            node1=int(lignei[0])
            node2=int(lignei[1])
            power_min=int(lignei[2])
            if len(lignei)>3:
                dist=int(lignei[3])
                G.add_edge(node1, node2, power_min, dist)
            else :

                G.add_edge(node1, node2, power_min)
    return G
