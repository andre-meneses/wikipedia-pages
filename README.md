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


## Network Metrics
