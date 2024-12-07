filePath = "input.txt"

with open(filePath, "r") as file:
    data = file.read()

def simulatePath(data):

    # Parse Input
    grid = [list(row) for row in data.splitlines()]
    rows, cols = len(grid), len(grid[0])

    # Directions -> Up, Down, Right, Left
    directions = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}
    directionOrder = ['^', '>', 'v', '<']

    # Locate guard's starting position and initial direction
    guardPos, guardDir = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guardPos = (r,c)
                guardDir = grid[r][c]
                grid[r][c] = '.'    # Clear guards stating position
                break

        if guardPos:
            break

    visited = set()
    visited.add(guardPos)

    while True:
        # Calculate next position based on the current direction
        dr, dc = directions[guardDir]
        nextPos = (guardPos[0] + dr, guardPos[1] + dc)

        # Check if the next position is out of bounds
        if not(0 <= nextPos[0] < rows and 0 <= nextPos[1] < cols):
            break

        # Check if there is any obstacle
        if grid[nextPos[0]][nextPos[1]] == "#":
            # Turn right by 90 degree
            currentIndex = directionOrder.index(guardDir)
            guardDir = directionOrder[(currentIndex + 1) % 4]

        else:
            # Move forward
            guardPos = nextPos
            visited.add(guardPos)

    return len(visited)


noVisited = simulatePath(data)
print(noVisited)


# Answer -> 4462