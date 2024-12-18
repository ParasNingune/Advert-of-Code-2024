import heapq

def parseInput(filePath):
    """Reads the input file and parses byte coordinates."""
    with open(filePath, 'r') as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def simulateMemorySpace(corruptCoords, gridSize):
    """Simulates the memory space after bytes have fallen."""
    memorySpace = [[False] * gridSize for _ in range(gridSize)]
    for x, y in corruptCoords:
        if 0 <= x < gridSize and 0 <= y < gridSize:
            memorySpace[y][x] = True
    return memorySpace

def findShortestPath(memorySpace, start, end):
    """Finds the shortest path in the memory space using A* algorithm."""
    gridSize = len(memorySpace)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def heuristic(x, y):
        return abs(x - end[0]) + abs(y - end[1])

    pq = [(0 + heuristic(*start), 0, start)]  # (priority, steps, position)
    visited = set()

    while pq:
        _, steps, (x, y) = heapq.heappop(pq)

        if (x, y) == end:
            return steps

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < gridSize and 0 <= ny < gridSize and not memorySpace[ny][nx] and (nx, ny) not in visited:
                heapq.heappush(pq, (steps + 1 + heuristic(nx, ny), steps + 1, (nx, ny)))

    return -1  # No path found

def findFirstBlockingByte(corruptCoords, gridSize, start, end):
    """Finds the first byte that blocks the path to the exit."""
    memorySpace = [[False] * gridSize for _ in range(gridSize)]
    
    for idx, (x, y) in enumerate(corruptCoords):
        if 0 <= x < gridSize and 0 <= y < gridSize:
            memorySpace[y][x] = True
            if findShortestPath(memorySpace, start, end) == -1:
                return x, y
    return None


# Input file path
filePath = "input.txt"

corruptCoords = parseInput(filePath)
gridSize = 71

# Find first blocking byte
start = (0, 0)
end = (gridSize - 1, gridSize - 1)
blockingByte = findFirstBlockingByte(corruptCoords, gridSize, start, end)

if blockingByte:
    print(f"{blockingByte[0]}, {blockingByte[1]}")
else:
    print("No byte blocks the path.")

# Answer -> 24,30