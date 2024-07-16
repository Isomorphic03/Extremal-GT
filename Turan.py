import networkx as nx
import matplotlib.pyplot as plt

def turan_graph(n, r):
   
    G = nx.Graph()
    vertices = list(range(n))
    G.add_nodes_from(vertices)
    
    # Divide vertices into r almost equal parts
    part_sizes = [n // r + (1 if i < n % r else 0) for i in range(r)]
    
    # Create partitions
    partitions = []
    current_index = 0
    for size in part_sizes:
        partitions.append(vertices[current_index:current_index + size])
        current_index += size
    
    # Add edges between vertices in different parts
    for i in range(r):
        for j in range(i + 1, r):
            for u in partitions[i]:
                for v in partitions[j]:
                    G.add_edge(u, v)
    
    return G

def draw_graph(G):
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()


