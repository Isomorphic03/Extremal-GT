import networkx as nx
import random
import matplotlib.pyplot as plt

def random_graph(n, p):
   
    if not (0 <= p <= 1):
        raise ValueError("Probability p must be between 0 and 1.")
    
    G = nx.Graph()
    G.add_nodes_from(range(n))
    
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:
                G.add_edge(u, v)
    
    return G

def draw_graph(G):
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

