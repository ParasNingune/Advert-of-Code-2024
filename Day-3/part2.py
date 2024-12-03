import re

filePath = "input.txt"

# Read file content
try:
    with open(filePath, "r") as file:
        memory = file.read()
except FileNotFoundError:
    print(f"Error: File '{filePath}' not found.")
    exit()

# Patterns for instructions
multiplicationPattern = r"mul\((\d+),\s*(\d+)\)"
statePattern = r"(do\(\)|don't\(\))"

# State tracking
flag = True
totalSum = 0

# Split into instructions
instructions = re.split(r"(?<=\))", memory)


# Process instructions
for instruction in instructions:
    # Check for state instructions
    stateMatch = re.search(statePattern, instruction)
    if stateMatch:
        if stateMatch.group() == "do()":
            flag = True
        elif stateMatch.group() == "don't()":
            flag = False
        continue

    # Check for multiplication instructions
    multiplicationMatch = re.search(multiplicationPattern, instruction)
    if multiplicationMatch and flag:
        x, y = map(int, multiplicationMatch.groups())
        result = x * y
        totalSum += result

# Final result
print(totalSum)

# Answer -> 107069718