from collections import defaultdict, deque
filePath = "input.txt"

with open(filePath, "r") as file:
    data = file.read()

# Splitting data into rules and updates
ruleSection, updateSection = data.strip().split("\n\n")

# Parse rules and updates
rules = [(int(x), int(y)) for x, y in (line.split("|") for line in ruleSection.splitlines())]
updates = [list(map(int, line.split(","))) for line in updateSection.splitlines()]

def correctUpdate(update, rules):
    graph = defaultdict(list)
    inDegree = defaultdict(int)
    nodes = set(update)

    # Build graph and inDegree for the updates relevant rules
    for x, y in rules:
        if x in nodes and y in nodes:
            graph[x].append(y)
            inDegree[y] += 1
            inDegree.setdefault(x, 0)

    # Topological sort
    queue = deque([node for node in nodes if inDegree[node] == 0])
    sortedUpdate = []

    while queue:
        current = queue.popleft()
        sortedUpdate.append(current)

        for neighbour in graph[current]:
            inDegree[neighbour] -= 1

            if inDegree[neighbour] == 0:
                queue.append(neighbour)

    return sortedUpdate

# Check if an update is correctly ordered
def updateOrder(updates):
    index = {page: i for i, page in enumerate(updates)}

    return all(index[x] < index[y] for x,y in rules if x in index and y in index)

sumIncorrectMiddlePages = sum(correctUpdate(update, rules)[len(update) // 2] for update in updates if not updateOrder(update))

print(sumIncorrectMiddlePages)

# Answer -> 6767