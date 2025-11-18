# Comparison of Search Algorithms on the Mexico City Metro Network


This project explores and compares different search algorithms by applying them to the real structure of the Mexico City Metro system. Using official data of stations, geographic coordinates, and track distances, the metro network is modeled as a weighted graph where each station is a node and each connection represents the distance in meters between stations.

The goal is to analyze how uninformed and informed search strategies behave when solving routing problems under two different criteria:

Finding a path with the minimum number of stations.

Finding the path with the minimum total distance in meters.

Description

The dataset consists of two CSV files:

estaciones.csv — station names, coordinates, and line information.

conexiones.csv — direct connections between stations and their distances.

With this data, the metro network is built and visualized using real geographic coordinates.

Algorithms Implemented

To compare different approaches to graph search, the following algorithms were implemented from scratch:

Breadth-First Search (BFS)

Used to find the path with the least number of stations. Since BFS expands nodes layer by layer, it guarantees the minimal number of edges between the start and end stations.

Dijkstra

Used to compute the shortest path in meters. Dijkstra explores nodes purely based on accumulated cost, guaranteeing the optimal route in terms of total distance.

A*

Also used to minimize total distance. A* incorporates a heuristic—in this case, the Haversine distance between station coordinates—which guides the search toward the target more efficiently. Because the heuristic never overestimates the true distance, A* remains optimal while expanding fewer nodes than Dijkstra.

Results and Analysis

BFS often produces completely different routes because it ignores real physical distances. Dijkstra and A* usually find the same optimal path, but A* is significantly more efficient thanks to the heuristic. In multiple tests across different station pairs, A* consistently explored fewer nodes, while still matching Dijkstra’s optimal route. BFS is only appropriate when the goal is minimizing the number of stations.

Files

notebook.ipynb — includes graph construction, visualization, and algorithm execution.

funciones.py — contains the BFS, Dijkstra, and A* implementations with node-count tracking.

estaciones.csv / conexiones.csv — dataset describing the metro system.

Summary

This project demonstrates how different search algorithms behave under different cost definitions. It highlights the efficiency advantages of informed search (A*) over uninformed search (BFS, Dijkstra) when a well-designed heuristic is available.
