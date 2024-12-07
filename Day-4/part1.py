filePath = "input.txt"

target = "XMAS"

# Reading the input
with open(filePath, "r") as file:
    grid = [line.strip() for line in file.readlines()]

# Define grid dimensions
rows = len(grid)
cols = len(grid[0])

# Define all possible 8 directions
directions = [
    (0,1),  # Right
    (1,0),  # Down
    (1,1),  # Diagonal Right-Down
    (1,-1), # Diagonal Left-Down
    (0,-1), # Left
    (-1,0), # Up
    (-1,-1), # Diagonal Left-Up
    (-1,1)  # Diagonal Right-Up
]

# Function to check if word exist in given direction
def checkWord(x, y, dx, dy):
    for i in range(len(target)):
        nx, ny = x + i*dx, y + i*dy

        # If boundaries and characters mathc
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != target[i]:
            return False
    return True

count = 0

# Iterate through each cell in the grid
for r in range(rows):
    for c in range(cols):

        # Check all 8 directions from the currrent cell
        for dx, dy in directions:
            if checkWord(r,c,dx,dy):
                count += 1

print(count)

# Answer -> 2547