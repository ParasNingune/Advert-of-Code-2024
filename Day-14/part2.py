import re

def parse_input(file_path):
    robots = []
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip())
            if match:
                x, y, vx, vy = map(int, match.groups())
                robots.append(((x, y), (vx, vy)))
    return robots

def move_robots(robots, width, height, reverse=False):
    new_positions = []
    for (x, y), (vx, vy) in robots:
        if reverse:
            vx, vy = -vx, -vy
        new_x = (x + vx) % width
        new_y = (y + vy) % height
        new_positions.append(((new_x, new_y), (vx, vy)))
    return new_positions

def bounding_box(robots):
    x_coords = [x for (x, y), _ in robots]
    y_coords = [y for (x, y), _ in robots]
    return min(x_coords), max(x_coords), min(y_coords), max(y_coords)

def print_grid(robots, width, height):
    grid = [["." for _ in range(width)] for _ in range(height)]
    for (x, y), _ in robots:
        grid[y][x] = "#"
    for row in grid:
        print("".join(row))

def find_alignment(file_path, width=101, height=103):
    robots = parse_input(file_path)
    previous_area = float('inf')
    time = 0

    while True:
        # Move robots
        robots = move_robots(robots, width, height)

        # Calculate bounding box
        min_x, max_x, min_y, max_y = bounding_box(robots)
        area = (max_x - min_x + 1) * (max_y - min_y + 1)

        # Check if the bounding box has expanded again
        if area > previous_area:
            # Alignment occurred in the previous step
            robots = move_robots(robots, width, height, reverse=True)
            time -= 1
            break

        previous_area = area
        time += 1

    # Print the grid to visually confirm the pattern
    print_grid(robots, width, height)
    return time

# Input file path
file_path = "input.txt"

# Find and print the time of alignment
res = find_alignment(file_path)
print("\n\n")
print(res)

# Answer -> 6587
