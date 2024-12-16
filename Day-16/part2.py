import heapq
from collections import deque

def parseInput(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def solve(mazeLines):
    rows = len(mazeLines)
    cols = len(mazeLines[0])

    directions = [
        (0, 1),   # East
        (1, 0),   # South
        (0, -1),  # West
        (-1, 0)   # North
    ]

    start = None
    end = None
    
    # Identify S and E
    for r in range(rows):
        for c in range(cols):
            ch = mazeLines[r][c]
            if ch == 'S':
                start = (r, c)
            elif ch == 'E':
                end = (r, c)
    if not start or not end:
        raise ValueError("Could not find 'S' or 'E' in the maze.")

    INF = float('inf')
    dist = [[[INF]*4 for _ in range(cols)] for __ in range(rows)]
    
    startDir = 0  # The reindeer start facing East = 0
    dist[start[0]][start[1]][startDir] = 0
    
    pq = [(0, start[0], start[1], startDir)]
    heapq.heapify(pq)
    visited = set()

    while pq:
        cost, r, c, d = heapq.heappop(pq)
        
        if (r, c, d) in visited:
            continue
        visited.add((r, c, d))

        currentDist = dist[r][c][d]
        if cost > currentDist:
            continue
        
        # 1) Move forward
        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and mazeLines[nr][nc] != '#':
            newCost = cost + 1
            if newCost < dist[nr][nc][d]:
                dist[nr][nc][d] = newCost
                heapq.heappush(pq, (newCost, nr, nc, d))
        
        # 2) Turn left
        leftDir = (d - 1) % 4
        newCost = cost + 1000
        if newCost < dist[r][c][leftDir]:
            dist[r][c][leftDir] = newCost
            heapq.heappush(pq, (newCost, r, c, leftDir))
        
        # 3) Turn right
        rightDir = (d + 1) % 4
        newCost = cost + 1000
        if newCost < dist[r][c][rightDir]:
            dist[r][c][rightDir] = newCost
            heapq.heappush(pq, (newCost, r, c, rightDir))

    # Find minimal cost to reach E (over all 4 directions)
    minCostEnd = min(dist[end[0]][end[1]][d] for d in range(4))

    # Mark all cells that lie on at least one best path
    bestPath = [[False]*cols for _ in range(rows)]

    # We'll do a reverse BFS from all (end, direction) states that achieve minCostEnd
    queue = deque()
    for d in range(4):
        if dist[end[0]][end[1]][d] == minCostEnd:
            queue.append((end[0], end[1], d))

    visitedRev = set(queue)
    
    while queue:
        r, c, d = queue.popleft()
        bestPath[r][c] = True
        
        cost_here = dist[r][c][d]
        
        dr, dc = directions[d]
        rPrev, c_prev = r - dr, c - dc
        if 0 <= rPrev < rows and 0 <= c_prev < cols:
            if mazeLines[rPrev][c_prev] != '#':
                if dist[rPrev][c_prev][d] == cost_here - 1:
                    if (rPrev, c_prev, d) not in visitedRev:
                        visitedRev.add((rPrev, c_prev, d))
                        queue.append((rPrev, c_prev, d))
        
        for dPrev in [(d - 1) % 4, (d + 1) % 4]:
            if dist[r][c][dPrev] == cost_here - 1000:
                if (r, c, dPrev) not in visitedRev:
                    visitedRev.add((r, c, dPrev))
                    queue.append((r, c, dPrev))

    # Count how many unique (r, c) got marked
    result = sum(bestPath[r][c] for r in range(rows) for c in range(cols))
    return result

mazeLines = parseInput("input.txt")
answer = solve(mazeLines)
print(answer)

# Answer -> 590