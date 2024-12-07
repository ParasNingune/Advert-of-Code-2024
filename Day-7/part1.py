from itertools import product
filePath = "input.txt"

with open(filePath, "r") as file:
    data = file.read()

# Function to evaluate the expression with operators between numbers
def evaluateExpressions(numbers, operators):
    result = numbers[0]

    for i, operator in enumerate(operators):
        if operator == "+":
            result += numbers[i+1]
        elif operator == "*":
            result *= numbers[i+1]

    return result

def parseInput(data):
    # Parses input data into list of equations

    equations = []

    for line in data.strip().split("\n"):
        if ":" not in line:
            continue
        target, numbers = line.strip().split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))

        equations.append((target, numbers))

    return equations

# Function to solve the puzzle
def totalResult(equations):

    validEquations = []
    operators = ["+", "*"]

    for target, numbers in equations:
        possible = False

        for operator in product(operators, repeat=len(numbers) - 1):
            if evaluateExpressions(numbers, operator) == target:
                possible = True
                break
        if possible:
            validEquations.append(target)

    return sum(validEquations)

equations = parseInput(data)
result = totalResult(equations)

print(result)

# Answer -> 1153997401072