filePath = "input.txt"

def parseInput(filePath):
    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    # First line contains available towel patterns
    towelPatterns = lines[0].split(', ')

    # Remaining lines after a blank line are the desired designs
    designs = lines[2:]  # Skip the first line and the blank line

    return towelPatterns, designs

def countWays(design, patterns, memo):
    if design in memo:
        return memo[design]

    if design == "":
        return 1  # One way to construct an empty design

    totalWays = 0
    for pattern in patterns:
        if design.startswith(pattern):
            remaining = design[len(pattern):]
            totalWays += countWays(remaining, patterns, memo)

    memo[design] = totalWays
    return totalWays

def totalArrangements(filePath):
    patterns, designs = parseInput(filePath)
    total = 0
    memo = {}

    for design in designs:
        total += countWays(design, patterns, memo)

    return total

res = totalArrangements(filePath)
print(res)

# Answer -> 584553405070389