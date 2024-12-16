from heapq import heappop, heappush

def parse_maze(maze):
    start = None
    end = None
    grid = []
    for y, line in enumerate(maze.splitlines()):
        row = list(line)
        grid.append(row)
        if "S" in row:
            start = (row.index("S"), y)
        if "E" in row:
            end = (row.index("E"), y)
    return grid, start, end

def reindeer_maze(maze):
    grid, start, end = parse_maze(maze)
    directions = ['E', 'S', 'W', 'N']
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    startState = (0, start[0], start[1], 0)  # (score, x, y, direction index)
    heap = [startState]
    visited = set()
    
    while heap:
        score, x, y, d = heappop(heap)
        
        if (x, y, d) in visited:
            continue
        visited.add((x, y, d))
        
        # Check if we reached the end
        if (x, y) == end:
            return score
        
        # Move forward
        dx, dy = moves[d]
        nx, ny = x + dx, y + dy
        if grid[ny][nx] != '#':
            heappush(heap, (score + 1, nx, ny, d))
        
        # Rotate clockwise and counterclockwise
        for nd in [(d + 1) % 4, (d - 1) % 4]:
            if (x, y, nd) not in visited:
                heappush(heap, (score + 1000, x, y, nd))



with open("input.txt", "r") as file:
    maze = file.read()

result = reindeer_maze(maze)
print(result)

# Answer -> 82460