from collections import Counter, defaultdict
filePath = "input.txt"

with open(filePath, "r") as file:

    data = file.read().strip().splitlines()

grid = {}

for row, line in enumerate(data):
    for col, tile in enumerate(line):
        grid[col + row * 1j] = tile

def floodFill(grid, start):
    # Initialize region with start position
    region = set([start])

    # Get symbol at start position
    symbol = grid[start]

    # Queue for breadth-first search
    queue = [start]

    # Breadth-first search
    while queue:
        # Get current position
        pos = queue.pop()

        # Check adjacent positions
        for d in [1, -1, 1j, -1j]:
            newPos = pos+d

            # Check if new position is valid and not explored
            if (newPos in grid and
                newPos not in region and
                grid[newPos] == symbol):
                region.add(newPos)
                queue.append(newPos)

    return region

def getArea(region):
    return len(region[1])

def getSideCount(region):
    perimeterEdges = set()

    for pos in region[1]:
        for direction in [1, -1, 1j, -1j]:
            new_pos = pos + direction
            if new_pos not in region[1]:
                perimeterEdges.add((new_pos, direction))

    distinct_sides = 0
    while len(perimeterEdges) > 0:
        # Pop a perimeter edge
        pos, direction = perimeterEdges.pop()
        distinct_sides += 1
        
        # Explore in current direction
        next_pos = pos + direction * 1j
        while (next_pos, direction) in perimeterEdges:
            perimeterEdges.remove((next_pos, direction))
            next_pos += direction * 1j
        
        # Explore in opposite direction
        next_pos = pos + direction * -1j
        while (next_pos, direction) in perimeterEdges:
            perimeterEdges.remove((next_pos, direction))
            next_pos += direction * -1j
    
    return distinct_sides

def calculatePrice(grid):
    regions = []
    unexplored = set(grid.keys())

    while len(unexplored) > 0:
        start = unexplored.pop()

        region = floodFill(grid, start)

        unexplored -= region

        regions.append((grid[start], region))

    
    price = 0
    for region in regions:
        area, perimeter = getArea(region), getSideCount(region)
        price += area*perimeter

    return price


resPrice = calculatePrice(grid)
print(resPrice)


# Answer -> 902742