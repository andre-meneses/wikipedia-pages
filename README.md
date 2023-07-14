# Wikipedia pages analysis

## Requisitos
- [ ] Generate a directed network from wikipedia pages' links. 
- [x] Pick a seed (wikipedia page)
- [ ] Generate network metrics plot 
- [ ] Generate KDE plot (degree and some other metric)
- [ ] Generate pair plot
- [ ] Generate shell and core plot
- [ ] Generate data pipeline 

## Introduction 

This project is a component of the Algorithm and Data Structure 2 course offered at the Federal University of Rio Grande do Norte. The main goal of this endeavor is to create a directed network (graph) using links from Wikipedia pages and conduct a comprehensive analysis using network concepts. The process of generating the network begins with a specific Wikipedia page and is limited to a depth level of 2. The selection of Gödel's incompleteness theorems  was made as the basis for generating the network.

## Data Pipeline
The data pipeline comprises four essential tasks. The initial node is responsible for fetching data from a specified seed and building the graph. The subsequent node eliminates any duplicate nodes, while the third node filters out nodes with a degree less than 2. Finally, the last node combines computations and generates plots for various network metrics, including degree centrality, closeness centrality, betweenness centrality, and eigenvector centrality.

<center><img width="800" src="figures/pipeline.svg"></center>

## Data Cleaning

The initial version of the directed graph generated from the "Godel Incompleteness Theorems" consisted of 24,342 nodes and 119,354 edges. After removing duplicates, the graph was refined to 24,090 nodes and 119,049 edges. Finally, by filtering out all nodes with a degree of one, the resulting graph was reduced to 5,447 nodes and 97,550 edges.

## Network Metrics

### Degree Centrality
Measures the number of connections (edges) that a node has in a network, relative to the total number of possible connections. It represents the importance or influence of a node based on the proportion of direct connections it has compared to all possible connections in the network. Nodes with higher degree centrality are often considered more central or influential in the network.

Top 10 nodes with higher degree centrality:
<center><img width="800" src="figures/degree_centrality.png"></center>

### Closeness Centrality
Quantifies how close a node is to all other nodes in a network. It measures the average shortest path length from a node to all other nodes. Nodes with high closeness centrality are typically able to reach other nodes quickly and efficiently, acting as information brokers or bridges in the network.

Top 10 nodes with higher closeness centrality:
<center><img width="800" src="figures/closeness_centrality.png"></center>

### Betweenness Centrality
Identifies nodes that act as intermediaries or bridges between other nodes in a network. It quantifies how often a node lies on the shortest paths between pairs of nodes. Nodes with high betweenness centrality have significant control over information flow and can facilitate communication between disparate parts of the network.

Top 10 nodes with higher betweenness centrality:
<center><img width="800" src="figures/betweenness_centrality.png"></center>


### Eigenvector Centrality
Assigns a measure of importance to nodes based on both their direct connections and the importance of those connections. It takes into account the centrality of a node's neighbors, assigning higher scores to nodes connected to other highly central nodes. Nodes with high eigenvector centrality are influential due to their connections to other influential nodes.

Top 10 nodes with higher eigenvector centrality:
<center><img width="800" src="figures/eigenvector_centrality.png"></center>
