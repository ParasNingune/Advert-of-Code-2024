filePath = "input.txt"

target = "XMAS"

# Reading the input
with open(filePath, "r") as file:
    grid = [line.strip() for line in file.readlines()]

# Define grid dimensions
rows = len(grid)
cols = len(grid[0])

# Function to count no of valid word counts
def find_X_WordCount():
    count = 0

    # Traverse the grid ensuring sapce for the neighbours
    for r in range(1, rows-1):
        for c in range(1, cols-1):

            # Get center
            center = grid[r][c]

            # Get corners
            top_left = grid[r-1][c-1]
            top_right = grid[r-1][c+1]
            bottom_left = grid[r+1][c-1]
            bottom_right = grid[r+1][c+1]

            # Check if "A" is in center and the corners match one of the valid patterns
            if center == "A" and (
                (top_left == "M" and top_right == "S" and bottom_left == "M" and bottom_right == "S") or
                (top_left == "S" and top_right == "M" and bottom_left == "S" and bottom_right == "M") or
                (top_left == "M" and top_right == "M" and bottom_left == "S" and bottom_right == "S") or
                (top_left == "S" and top_right == "S" and bottom_left == "M" and bottom_right == "M")
            ):
                count += 1

    return count
                

count = find_X_WordCount()
print(count)

# Answer -> 1939