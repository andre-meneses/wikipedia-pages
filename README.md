# Wikipedia pages analysis

## Introduction 

This project is a component of the Algorithm and Data Structure 2 course offered at the Federal University of Rio Grande do Norte. The main goal of this endeavor is to create a directed network (graph) using links from Wikipedia pages and conduct a comprehensive analysis using network concepts. The process of generating the network begins with a specific Wikipedia page and is limited to a depth level of 2. The selection of Gödel's incompleteness theorems  was made as the basis for generating the network.

## Data Pipeline
The data pipeline comprises four essential tasks. The initial node is responsible for fetching data from a specified seed and building the graph. The subsequent node eliminates any duplicate nodes, while the third node filters out nodes with a degree less than 2. Finally, the last node combines computations and generates plots for various network metrics, including degree centrality, closeness centrality, betweenness centrality, and eigenvector centrality.

<center><img width="800" src="figures/pipeline.svg"></center>

## Run the notebook
To replicate the presented results, simply execute the notebook and modify the page title to the desired one.
```
pipeline.run("Wikipedia Page")

```
## Loom video
- Parte I (Unidade II) - [:camera: video](https://www.loom.com/share/11f668624d8c41ab9542e609c54b01c3?sid=4965e1e5-29ba-4a09-a2a6-8b6b7afc7ece)
- Parte II (Unidade III) - [:camera: video](https://www.loom.com/share/5227fed92e034827ad6b575cd5edd47d?sid=31c0c75f-57a2-4173-9660-54a62952572d)

## Data Cleaning

The initial version of the directed graph generated from the "Godel Incompleteness Theorems" consisted of 24,342 nodes and 119,354 edges. After removing duplicates, the graph was refined to 24,090 nodes and 119,049 edges. Finally, by filtering out all nodes with a degree of one, the resulting graph was reduced to 5,447 nodes and 97,550 edges.

## Network Metrics

### Degree Centrality
Measures the number of connections (edges) that a node has in a network, relative to the total number of possible connections. It represents the importance or influence of a node based on the proportion of direct connections it has compared to all possible connections in the network. Nodes with higher degree centrality are often considered more central or influential in the network.

Top 10 nodes with higher degree centrality:
<center><img width="800" src="figures/degree_centrality.png"></center>

### Closeness Centrality
Quantifies how close a node is to all other nodes in a network. It measures the average shortest path length from a node to all other nodes. Nodes with high closeness centrality are typically able to reach other nodes quickly and efficiently, acting as information brokers or bridges in the network.

Below are the top 10 nodes that exhibit a higher degree centrality:
<center><img width="800" src="figures/closeness_centrality.png"></center>

### Betweenness Centrality
Identifies nodes that act as intermediaries or bridges between other nodes in a network. It quantifies how often a node lies on the shortest paths between pairs of nodes. Nodes with high betweenness centrality have significant control over information flow and can facilitate communication between disparate parts of the network.

Below are the top 10 nodes that exhibit a higher betweenness centrality:
<center><img width="800" src="figures/betweenness_centrality.png"></center>


### Eigenvector Centrality
Assigns a measure of importance to nodes based on both their direct connections and the importance of those connections. It takes into account the centrality of a node's neighbors, assigning higher scores to nodes connected to other highly central nodes. Nodes with high eigenvector centrality are influential due to their connections to other influential nodes.

Below are the top 10 nodes that exhibit a higher eigenvector centrality:
<center><img width="800" src="figures/eigenvector_centrality.png"></center>

### K-core and K-shell
The greatest k-core within this network was determined to be 393, signifying a highly connected group of nodes. This k-core represents a cohesive subset of pages that are intricately interconnected with each other.

Furthermore, the greatest k-shell within this network was found to have a value of 294. A k-shell refers to a subset of nodes that possess a minimum degree within the network. In this case, the k-shell of 294 represents a significant group of nodes with a minimal number of connections to the rest of the network.

These discoveries shed light on the intricate structure and interdependencies within the network of Wikipedia pages stemming from the Gödel Incompleteness Theorems. The existence of such a robust k-core and k-shell underscores the interconnected nature of the topics and concepts associated with this prominent mathematical theorem.

<center><img width="800" src="figures/k-core_sociopatterns.png"></center>

## Probability Distributions 
Firstly, focusing on the degree distribution, the probability density function (PDF) reveals that the majority of nodes exhibit degrees ranging from 0 to 50. This suggests that a significant portion of pages within the network have relatively low connectivity. However, intriguingly, there is a small curve in the PDF that emerges between the range of 400 and 600. This indicates the presence of a subset of nodes with notably high degrees, signifying a group of pages with a substantial number of connections. These nodes with high degrees play a crucial role in facilitating information flow and connecting disparate topics within the network.

Similarly, when examining the PDF of eigenvector centrality, a similar trend emerges. The majority of nodes are distributed around low values of eigenvector centrality, indicating that most pages have limited influence or prominence within the network. However, there are notable exceptions, as evidenced by the presence of nodes with high eigenvector centrality values. These nodes hold significant importance in terms of their influence and centrality within the network, likely representing key topics or foundational concepts that have a widespread impact on other pages.

In summary, the probability distributions of the degree and eigenvector centrality within the network of Wikipedia pages starting from the Gödel Incompleteness Theorems demonstrate a pattern of most nodes having low values, while a subset of nodes exhibit high degrees and eigenvector centrality. These distributions highlight the varying levels of connectivity and influence within the network, emphasizing the significance of certain nodes in shaping the overall structure and flow of information within this domain.

<center><img width="800" src="figures/degree_and_centrality_plots.png"></center>

## Pair Plot with network metrics
Upon examining the pair plot of network metrics within the directed network of Wikipedia pages, starting from the Gödel Incompleteness Theorems, some intriguing patterns have emerged. While the pair plot may not provide comprehensive insights into the network's overall structure, it does reveal notable correlations between certain metrics and suggests the presence of distinct clusters within the data.

Firstly, the pair plot indicates a correlation between betweenness and degree. This correlation implies that nodes with higher degrees tend to have a greater influence in terms of information flow within the network. Nodes with higher degrees often act as crucial bridges, connecting disparate topics and facilitating the transfer of knowledge across different areas.

Similarly, the pair plot reveals a correlation between eigenvector centrality and closeness. This correlation suggests that nodes with higher eigenvector centrality tend to have a closer proximity to other nodes within the network. This proximity allows these nodes to have more efficient and direct access to information, enhancing their overall centrality and influence within the network.

Moreover, the eigenvector column in the pair plot demonstrates the presence of two distinct clusters. The first cluster represents more popular nodes, characterized by higher eigenvector centrality values. These popular nodes likely correspond to topics or concepts that have garnered significant attention and prominence within the network. Conversely, the second cluster represents a larger group of nodes that are relatively less popular, with lower eigenvector centrality values. These nodes may correspond to less widely known or niche topics within the network.

<center><img width="800" src="figures/all.png"></center>

## Gephi Plots

### Visualization 
- [:chart: Github page with interactive network](https://andre-meneses.github.io/networkdeploy/network/)

Using the Gephi software, an improved visualization of the complete network was generated, leading to a visually captivating plot. The nodes were assigned colors corresponding to their respective communities, which were determined using modularity with a resolution of 1.0. The network consists of 9 distinct communities, distributed as follows:

1. Pink: Constituting 24.55% of the nodes
2. Green: Comprising 22.25% of the nodes
3. Blue: Accounting for 17.46% of the nodes
4. Other communities: Representing 35.74% of the nodes

Nodes with an in-degree exceeding 250 are identified by displaying their names, while the size of each node is scaled proportionally to its in-degree.  

<center><img width="800" src="figures/gephi_graph.svg"></center>

---- 

### Filtered Graphs

By examining the plot, it becomes apparent that there is a noticeable cluster of pink nodes with a high degree of connectivity. Conversely, the edges of the graph display numerous nodes with lower degrees. By filtering the graph taking into account the in-degree, only a percentege of nodes and edges are displayed:

<div align="center">

| In-Degree | Nodes    | Edges   |
| --------- | -----    | -----   |
| 4         | 69.68%   | 93.53%  |
| 5         | 49.78%   | 87.15%  |
| 10        | 22.33%   | 74.85%  |
| 15        | 12.76%   | 67.25%  |
| 30        | 07.45%   | 61.68%  |
| 80        | 04.92%   | 54.10%  |

</div>

#### Graph with in-degree > 80

<center><img width="800" src="figures/gephi_graph_80_in.svg"></center>

### K-core

It is possible to use gephi to plot the 343-core as well:

<center><img width="800" src="figures/gephi_graph_core.svg"></center>

## Gephisto Visualization
By using the [enhanced.graphml](./graphml/enhanced.graphml) file, we used [gephisto](https://jacomyma.github.io/gephisto/) to generate another visualization of the graph. We can now see different nodes displayed and a different color scheme, which gives a different perspective on the network .

<center><img width="800" src="figures/gephisto.png"></center>

