from collections import defaultdict
import networkx as nx

with open("input.txt", "r") as file:
    data = file.read().split("\n")

data = [i.split("-") for i in data]

trios = {}
nodes = defaultdict(list)

for i in data:
    nodes[i[0]].append(i[1])
    nodes[i[1]].append(i[0])
for i in nodes:
    for j in nodes[i]:
        for k in nodes:
            if k == i or k==j:
                continue
            if k in nodes[i] and k in nodes[j]:
                trios[tuple(sorted([i,j,k]))] = True
count = 0
for i in trios:
    for j in i:
        if j[0] == "t":
            count+=1
            break
print(count)
G = nx.Graph()

G.add_nodes_from(nodes.keys())
for i in nodes:
    for j in nodes[i]:
        G.add_edge(i,j)

print(",".join(sorted(max(nx.algorithms.clique.find_cliques(G), key = len))))