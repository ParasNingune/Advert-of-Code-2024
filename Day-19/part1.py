filePath = "input.txt"

def parseInput(filePath):
    with open(filePath, 'r') as f:
        lines = f.read().splitlines()

    # First line contains available towel patterns
    towel_patterns = lines[0].split(', ')

    # Remaining lines after a blank line are the desired designs
    designs = lines[2:]  # Skip the first line and the blank line

    return towel_patterns, designs

def can_construct(design, patterns, memo):
    if design in memo:
        return memo[design]

    if design == "":
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            remaining = design[len(pattern):]
            if can_construct(remaining, patterns, memo):
                memo[design] = True
                return True

    memo[design] = False
    return False

def countPossibledesigns(filePath):
    patterns, designs = parseInput(filePath)
    count = 0
    memo = {}

    for design in designs:
        if can_construct(design, patterns, memo):
            count += 1

    return count

# Example usage # Replace with your file path
res = countPossibledesigns(filePath)

print(res)

# Answer -> 228