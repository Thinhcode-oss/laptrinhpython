import networkx as nx
import matplotlib.pyplot as plt

# code lab 2

def draw_graph(graph_matrix, colors, n):
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(i+1, n):
            if graph_matrix[i][j] == 1:
                G.add_edge(i, j)
    node_colors = []
    for i in range(n):
        node_colors.append(colors[i])
    pos = nx.spring_layout(G, seed=42)
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=node_colors,
        cmap=plt.cm.tab10,
        node_size=800,
        font_color="white"
    )
    plt.show()
    
draw_graph(graph, colors, n)