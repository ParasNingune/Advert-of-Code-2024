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

def getPerimeter(region):
    perimeter = 0
    for pos in region[1]:
        for d in [1, -1, 1j, -1j]:
            new_pos = pos + d
            # Count edges that are outside the region
            if new_pos not in region[1]:
                perimeter += 1
    return perimeter

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
        area, perimeter = getArea(region), getPerimeter(region)
        price += area*perimeter

    return price


resPrice = calculatePrice(grid)
print(resPrice)


# Answer -> 1446042