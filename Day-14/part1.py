filePath = "input.txt"

GRIDWIDTH = 101
GRIDHEIGHT = 103
SIMULATIONTIME = 100


robots = []
with open(filePath, "r") as file:
    for line in file:
        parts = line.strip().split(' ')
        px, py = map(int, parts[0][2:].split(','))
        vx, vy = map(int, parts[1][2:].split(','))
        robots.append({"p": (px, py), "v": (vx, vy)})


finalPositions = []
for robot in robots:
    px, py = robot["p"]
    vx, vy = robot["v"]

    finalX = (px+vx*SIMULATIONTIME) % GRIDWIDTH
    finalY = (py+vy*SIMULATIONTIME) % GRIDHEIGHT

    finalPositions.append((finalX, finalY))

midX = GRIDWIDTH // 2
midY = GRIDHEIGHT // 2

quadrantCounts = [0, 0, 0, 0]  # Quadrants 1, 2, 3, 4
for x, y in finalPositions:
    if x == midX or y == midY:
        continue  # Skip robots exactly on the middle lines
    if x > midX and y <= midY:
        quadrantCounts[0] += 1  # Quadrant 1
    elif x <= midX and y <= midY:
        quadrantCounts[1] += 1  # Quadrant 2
    elif x <= midX and y > midY:
        quadrantCounts[2] += 1  # Quadrant 3
    elif x > midX and y > midY:
        quadrantCounts[3] += 1  # Quadrant 4

safetyFactor = 1
for count in quadrantCounts:
    safetyFactor *= count

print(safetyFactor)

# Answer -> 211692000