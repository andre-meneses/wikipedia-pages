import seaborn as sns
import matplotlib.pyplot as plt

def plot_centrality(subgraph, pos, centrality_measure, filename):
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    # Color of nodes based on centrality measure
    color = list(dict(centrality_measure(subgraph)).values())

    # Draw edges
    nx.draw_networkx_edges(subgraph, pos=pos, alpha=0.4, ax=ax)

    # Draw nodes
    nodes = nx.draw_networkx_nodes(subgraph, pos=pos, node_color=color, cmap=plt.cm.jet, ax=ax)

    # Draw labels
    nx.draw_networkx_labels(subgraph, pos=pos, font_color='white', font_size=4, ax=ax)

    plt.axis("off")
    plt.colorbar(nodes)
    plt.savefig(filename, transparent=True, dpi=300)
    plt.show()


def plot_degree_centrality(subgraph, pos):
    plot_centrality(subgraph, pos, nx.degree_centrality, 'degree_centrality.png')


def plot_closeness_centrality(subgraph, pos):
    plot_centrality(subgraph, pos, nx.closeness_centrality, 'closeness_centrality.png')


def plot_betweenness_centrality(subgraph, pos):
    plot_centrality(subgraph, pos, nx.betweenness_centrality, 'betweenness_centrality.png')


def plot_eigenvector_centrality(subgraph, pos):
    plot_centrality(subgraph, pos, nx.eigenvector_centrality, 'eigenvector_centrality.png')


def plot_pdf(subgraph):
    plt.style.use("fivethirtyeight")
    #plt.style.use("default")
    degree_sequence = sorted([d for n, d in subgraph.degree()], reverse=True) 
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    sns.histplot(degree_sequence, bins=7, label="Count", ax=ax)
    ax2 = ax.twinx()
    sns.kdeplot(degree_sequence, color='r', label="Probability Density Function (PDF)", ax=ax2)

    # Ask matplotlib for the plotted objects and their labels
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc=0)

    ax.grid(False)
    ax2.grid(False)
    ax.set_xlabel("Degree")
    ax2.set_ylabel("Probability")

    plt.savefig('probability_density_function.png', transparent=True, dpi=600, bbox_inches="tight")
    plt.show()

