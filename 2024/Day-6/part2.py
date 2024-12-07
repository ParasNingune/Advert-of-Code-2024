import time

def load(file):
    with open(file) as f:
        return {(x, y): char for y, line in enumerate(f.read().split('\n')) for x, char in enumerate(line)}

def moveGuard(p, guardPos, guardDir):
    distinctPos = set()
    counter = 0
    while True:
        (x, y), (dx, dy) = guardPos, guardDir
        nx, ny = x + dx, y + dy

        if (nx, ny) not in p:
            return distinctPos
        if counter > 1000:
            return 'loop'

        if p[nx, ny] == '#':
            guardDir = -dy, dx
        else:
            guardPos = nx, ny
            if (nx, ny) in distinctPos:
                counter += 1
            else:
                counter = 0
            distinctPos.add((nx, ny))

def solve(p):
    part1 = part2 = 0
    guardPos = [pos for pos, char in p.items() if char == '^'][0]
    guardDir = (0, -1)

    distinctPos = moveGuard(p, guardPos, guardDir)
    part1 = len(distinctPos) + 1  # Include the starting position

    for x, y in distinctPos:
        p[x, y] = '#'
        if moveGuard(p, guardPos, guardDir) == 'loop':
            part2 += 1
        p[x, y] = '.'

    return part1, part2

def countObstructionPositions(file):
    # Start time measurement
    startTime = time.perf_counter()
    
    # Load the grid from the file
    p = load(file)
    
    # Find the starting position of the guard
    guardPos = [pos for pos, char in p.items() if char == '^'][0]
    guardDir = (0, -1)

    # Run guard simulation and get distinct positions
    distinctPos = moveGuard(p, guardPos, guardDir)

    validObstructions = 0

    # Check all positions around the distinct guard path
    for x, y in distinctPos:
        p[x, y] = '#'
        
        # Check if adding an obstruction causes the guard to get stuck in a loop
        if moveGuard(p, guardPos, guardDir) == 'loop':
            validObstructions += 1
        
        # Remove the obstruction for next check
        p[x, y] = '.'

    # End time measurement
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    
    return validObstructions, elapsedTime

# Example usage
filePath = "input.txt"
obstructionCount, timeTaken = countObstructionPositions(filePath)

print(obstructionCount)
print(f'{timeTaken:.5f} seconds')

# Answer -> 1946