from collections import deque

def solve_part2():
    input_filename = "input.txt"
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

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def is_track(ch):
        return ch in ('.', 'S', 'E')

    # BFS to find shortest dist from a given start point
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

    dist_from_S = bfs(start)
    dist_from_E = bfs(end)

    normal_dist = dist_from_S[end[0]][end[1]]
    if normal_dist == float('inf'):
        # No normal path means no cheats can help
        print(0)
        return

    cheats = set()

    # Pre-collect all track cells that are reachable from S to limit starting points
    track_cells_from_S = [(x,y) for x in range(rows) for y in range(cols) 
                          if dist_from_S[x][y] != float('inf') and is_track(grid[x][y])]

    for (sx, sy) in track_cells_from_S:
        # BFS ignoring walls from (sx, sy) up to distance 20
        dist_ignore_walls = [[float('inf')] * cols for _ in range(rows)]
        dist_ignore_walls[sx][sy] = 0
        q = deque([(sx, sy)])
        while q:
            x, y = q.popleft()
            d = dist_ignore_walls[x][y]
            if d == 20:
                # Can't go further than 20 steps
                continue
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    # ignoring walls, so no condition except bounds
                    if dist_ignore_walls[nx][ny] > d + 1:
                        dist_ignore_walls[nx][ny] = d+1
                        q.append((nx, ny))

        # Now check all track cells reachable within ≤20 steps
        base_dist = dist_from_S[sx][sy]
        for fx in range(rows):
            for fy in range(cols):
                d = dist_ignore_walls[fx][fy]
                if d != float('inf') and 1 <= d <= 20 and is_track(grid[fx][fy]):
                    # We have a potential cheat from (sx, sy) to (fx, fy) of length d
                    if dist_from_E[fx][fy] != float('inf'):
                        route_with_cheat = base_dist + d + dist_from_E[fx][fy]
                        saving = normal_dist - route_with_cheat
                        if saving >= 100:
                            cheats.add((sx, sy, fx, fy))

    print(len(cheats))


solve_part2()


# Answer -> 1000697