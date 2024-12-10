from collections import deque
filePath = "input.txt"

grid = []
with open(filePath, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            grid.append([int(char) for char in line])

def neightbours(r, c, rows, cols):
    # Return Up/Down/Left/Right neighbours
    for nr, nc in [(r-1,c), (r+1,c), (r, c-1), (r, c+1)]:
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def findTailHeadScores(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    tailHeads = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

    totalScore = 0

    for startR, startC in tailHeads:
        visited = set()
        queue = deque()
        queue.append((startR, startC))
        visited.add((startR, startC))

        reachableNines = set()

        while queue:
            r,c = queue.popleft()
            currentHeight = grid[r][c]

            if currentHeight == 9:
                reachableNines.add((r,c))

            else:
                nextHeight = currentHeight + 1
                for nr, nc in neightbours(r, c, rows, cols):
                    if (nr, nc) not in visited and grid[nr][nc] == nextHeight:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        tailHeadScore = len(reachableNines)
        totalScore += tailHeadScore

    return totalScore
    
res = findTailHeadScores(grid)
print(res)

# Answer -> 674