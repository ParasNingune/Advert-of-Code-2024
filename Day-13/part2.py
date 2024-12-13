from sympy import symbols, Eq, solve
import re

# Define variables for calculations
a, b = symbols('a b', integer=True)

# Function to parse machine data from multi-line input
def parse_multiline_machine(lines):
    if len(lines) == 3:
        button_a = re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])
        button_b = re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])
        prize = re.match(r"Prize: X=(\d+), Y=(\d+)", lines[2])
        if button_a and button_b and prize:
            return tuple(map(int, button_a.groups() + button_b.groups() + prize.groups()))
    return None

# Function to compute solutions for a list of machines
def compute_solutions(machines, offset_x=0, offset_y=0):
    results = []
    for Ax, Ay, Bx, By, Px, Py in machines:
        # Apply offset if provided
        Px += offset_x
        Py += offset_y
        
        # Solve the system of equations
        eq1 = Eq(a * Ax + b * Bx, Px)
        eq2 = Eq(a * Ay + b * By, Py)
        solutions = solve((eq1, eq2), (a, b), dict=True)
        valid_solutions = [
            (sol[a], sol[b]) for sol in solutions if sol[a] >= 0 and sol[b] >= 0
        ]
        
        # Find the minimum token cost
        min_cost = float('inf')
        best_sol = None
        for sol_a, sol_b in valid_solutions:
            cost = 3 * sol_a + sol_b
            if cost < min_cost:
                min_cost = cost
                best_sol = (sol_a, sol_b)
        if best_sol:
            results.append((min_cost, best_sol))

    # Calculate total cost and machines solved
    results.sort()
    total_cost = sum(cost for cost, _ in results)
    machines_solved = len(results)

    return total_cost, machines_solved


inputFile = "input.txt"  # Adjust this to the actual file path

# Parse input data
with open(inputFile, 'r') as f:
    raw_lines = [line.strip() for line in f if line.strip()]

# Group every 3 lines into a machine
machines = [parse_multiline_machine(raw_lines[i:i+3]) for i in range(0, len(raw_lines), 3)]
parsed_machines = [machine for machine in machines if machine is not None]

# Part 2: Solve with large offsets
OFFSET = 10_000_000_000_000
part2_total_cost, part2_machines_solved = compute_solutions(parsed_machines, offset_x=OFFSET, offset_y=OFFSET)

print(part2_total_cost)

# Answer -> 92827349540204