# Reading the input data from a text file
file_path = "input.txt"

# Load connections into a list of tuples
with open(file_path, "r") as file:
    connections = [line.strip().split("-") for line in file.readlines()]

# Building the adjacency list to represent the graph
from collections import defaultdict

graph = defaultdict(set)
for a, b in connections:
    graph[a].add(b)
    graph[b].add(a)  # since the connections are bidirectional

# Finding all triangles (sets of three interconnected computers)
triangles = set()
for node in graph:
    for neighbor in graph[node]:
        common_neighbors = graph[node].intersection(graph[neighbor])
        for cn in common_neighbors:
            triangle = tuple(sorted([node, neighbor, cn]))
            triangles.add(triangle)

# Filtering triangles with at least one computer name starting with 't'
filtered_triangles = [triangle for triangle in triangles if any(comp.startswith('t') for comp in triangle)]

# Output results
print(len(filtered_triangles))
