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

def countPaths(r,c, grid, dp, rows, cols):
    if dp[r][c] != -1:
        return dp[r][c]

    currentHeight = grid[r][c]

    # Base case: if height is 9, exactly one trail ends here
    if currentHeight == 9:
        dp[r][c] = 1
        return 1

    # Otherwise, sum over neighbors with height current_height+1
    totalPaths = 0
    nextHeight = currentHeight + 1
    for nr, nc in neightbours(r, c, rows, cols):
        if grid[nr][nc] == nextHeight:
            totalPaths += countPaths(nr, nc, grid, dp, rows, cols)

    dp[r][c] = totalPaths
    return totalPaths



rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# Identify all trailheads (cells with height 0)
trailheads = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

# dp[r][c] = number of distinct hiking trails from cell (r, c) to any height-9 cell
dp = [[-1]*cols for _ in range(rows)]

totalRating = 0
for (tr, tc) in trailheads:
    rating = countPaths(tr, tc, grid, dp, rows, cols)
    totalRating += rating

print(totalRating)

# Answer -> 1372