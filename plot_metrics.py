import seaborn as sns
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def plot_centrality(subgraph, centrality_measure, filename):
 # Calculate centrality values for all nodes in the subgraph
    centrality_values = centrality_measure(subgraph)

    # Sort nodes based on centrality values and select top 50 nodes
    top_nodes = sorted(centrality_values, key=centrality_values.get, reverse=True)[:10]

    # Create a subgraph with top nodes and their neighbors
    subgraph_top = subgraph.subgraph(top_nodes + list(subgraph.neighbors(n) for n in top_nodes))

    # Use the kamada_kawai_layout for the positions of the nodes
    pos = nx.kamada_kawai_layout(subgraph_top)

    # Adjust node spacing
    pos = {node: (x, y*5) for node, (x, y) in pos.items()}

    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    # Color of nodes based on centrality measure
    color = list(dict(centrality_measure(subgraph_top)).values())

    # Draw edges
    nx.draw_networkx_edges(subgraph_top, pos=pos, alpha=0.4, ax=ax)

    # Draw nodes
    nodes = nx.draw_networkx_nodes(subgraph_top, pos=pos, node_color=color, cmap=plt.cm.jet, ax=ax)

    # Draw labels
    nx.draw_networkx_labels(subgraph_top, pos=pos, font_color='black', font_size=8, ax=ax)

    plt.axis("off")
    plt.colorbar(nodes)
    plt.savefig(filename, transparent=True, dpi=300)
    plt.show()
    
def plot_degree_centrality(subgraph):
    plot_centrality(subgraph, nx.degree_centrality, 'degree_centrality.png')

def plot_closeness_centrality(subgraph):
    plot_centrality(subgraph, nx.closeness_centrality, 'closeness_centrality.png')


def plot_betweenness_centrality(subgraph):
    plot_centrality(subgraph, nx.betweenness_centrality, 'betweenness_centrality.png')


def plot_eigenvector_centrality(subgraph):
    plot_centrality(subgraph, nx.eigenvector_centrality, 'eigenvector_centrality.png')

def plot_degree_and_centrality(subgraph):
    plt.style.use("fivethirtyeight")
    degree_sequence = sorted([d for n, d in subgraph.degree()], reverse=True)
    eigenvector_centrality = list(nx.eigenvector_centrality(subgraph).values())

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    # Plot degree CDF
    sns.histplot(degree_sequence, bins=30, cumulative=True, stat="density", ax=axes[0])
    sns.kdeplot(degree_sequence, cumulative=True, color='r', ax=axes[0])
    axes[0].set_xlabel("Degree")
    axes[0].set_ylabel("CDF")

    # Plot degree PDF
    sns.histplot(degree_sequence, bins=30, stat="density", ax=axes[1])
    sns.kdeplot(degree_sequence, color='r', ax=axes[1])
    axes[1].set_xlabel("Degree")
    axes[1].set_ylabel("PDF")

    # Plot eigenvector centrality CDF
    sns.histplot(eigenvector_centrality, bins=30, cumulative=True, stat="density", ax=axes[2])
    sns.kdeplot(np.array(eigenvector_centrality), cumulative=True, color='r', ax=axes[2])
    axes[2].set_xlabel("Eigenvector Centrality")
    axes[2].set_ylabel("CDF")

    # Plot eigenvector centrality PDF
    sns.histplot(eigenvector_centrality, bins=30, stat="density", ax=axes[3])
    sns.kdeplot(np.array(eigenvector_centrality), color='r', ax=axes[3])
    axes[3].set_xlabel("Eigenvector Centrality")
    axes[3].set_ylabel("PDF")

    plt.tight_layout()
    plt.savefig('degree_and_centrality_plots.png', transparent=True, dpi=600, bbox_inches="tight")
    plt.show() 

