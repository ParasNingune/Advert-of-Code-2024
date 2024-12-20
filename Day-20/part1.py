from collections import deque

def solve():
    # The file name is stored in a variable, let's assume it's input_filename
    input_filename = "input.txt"

    # Read the map from the file
    with open(input_filename, 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    # Find S and E
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    # Directions for movement
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def is_track(ch):
        # 'S', 'E', '.' are considered track
        return ch in ('.', 'S', 'E')

    # BFS function to find shortest dist from a given start point
    def bfs(start_pos):
        dist = [[float('inf')] * cols for _ in range(rows)]
        sr, sc = start_pos
        dist[sr][sc] = 0
        queue = deque([start_pos])
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if is_track(grid[nx][ny]) and dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
        return dist

    # Get dist_from_S and dist_from_E
    dist_from_S = bfs(start)
    dist_from_E = bfs(end)

    # Normal shortest path from S to E
    normal_dist = dist_from_S[end[0]][end[1]]
    if normal_dist == float('inf'):
        # If there's no normal path from S to E, then no cheat can help.
        print(0)
        return

    cheats = set()  # to store (sx, sy, ex, ey)
    count = 0

    for x in range(rows):
        for y in range(cols):
            # Only consider this cell as a cheat start if it's reachable and is track
            if dist_from_S[x][y] == float('inf'):
                continue
            if not is_track(grid[x][y]):
                continue

            base_dist = dist_from_S[x][y]
            # 1-step cheat
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    # ignoring walls for the cheat step, so no condition here except inside bounds
                    if is_track(grid[nx][ny]):
                        # end_node = (nx, ny)
                        # Check if end_node is reachable from E
                        if dist_from_E[nx][ny] != float('inf'):
                            route_with_cheat = base_dist + 1 + dist_from_E[nx][ny]
                            saving = normal_dist - route_with_cheat
                            if saving >= 100:
                                # record cheat
                                if (x,y,nx,ny) not in cheats:
                                    cheats.add((x,y,nx,ny))

            # 2-step cheat
            # For each direction for the first step:
            for dx1, dy1 in directions:
                ix, iy = x+dx1, y+dy1
                if 0 <= ix < rows and 0 <= iy < cols:
                    # first step can go through walls as well
                    # second step:
                    for dx2, dy2 in directions:
                        fx, fy = ix+dx2, iy+dy2
                        if 0 <= fx < rows and 0 <= fy < cols:
                            # final cell must be track
                            if is_track(grid[fx][fy]):
                                if dist_from_E[fx][fy] != float('inf'):
                                    route_with_cheat = base_dist + 2 + dist_from_E[fx][fy]
                                    saving = normal_dist - route_with_cheat
                                    if saving >= 100:
                                        if (x,y,fx,fy) not in cheats:
                                            cheats.add((x,y,fx,fy))

    # Count the number of cheats with at least 100 saving
    print(len(cheats))


solve()

# Answer -> 1426