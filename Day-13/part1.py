filePath = "input.txt"

def parseInput(filePath):
    machines = []
    with open(filePath, 'r') as file:
        lines = file.read().strip().split("\n\n")  # Separate each machine by blank lines
        for block in lines:
            lines = block.splitlines()
            A = tuple(map(int, lines[0].split("X+")[1].split(", Y+")))
            B = tuple(map(int, lines[1].split("X+")[1].split(", Y+")))
            P = tuple(map(int, lines[2].split("X=")[1].split(", Y=")))
            machines.append({"A": A, "B": B, "P": P})
    return machines

def findMinCost(A, B, P, max_presses=100):
    Ax, Ay = A
    Bx, By = B
    Px, Py = P
    min_cost = float('inf')
    foundSolution = False

    # Iterate over possible values of a (number of A presses)
    for a in range(max_presses + 1):
        # Solve for b in both equations
        if (Px - a * Ax) % Bx == 0 and (Py - a * Ay) % By == 0:
            bx = (Px - a * Ax) // Bx
            by = (Py - a * Ay) // By

            # Check if b_x and b_y are equal and non-negative
            if bx == by and bx >= 0:
                foundSolution = True
                cost = 3 * a + bx
                min_cost = min(min_cost, cost)

    return min_cost if foundSolution else None


machines = parseInput(filePath)
resultFiles = [findMinCost(machine["A"], machine["B"], machine["P"]) for machine in machines]

totalCost = sum(cost for cost in resultFiles if cost is not None)
print(totalCost)

# Answer -> 30413