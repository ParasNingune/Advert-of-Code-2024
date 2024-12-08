from collections import defaultdict
filePath = "input.txt"

def parseMap(inputLines):
    charMap = {}
    positions = []

    for y, row in enumerate(inputLines):
        for x, char in enumerate(row):
            charMap[(x, y)] = char
            positions.append((x,y))

    return charMap, positions

def addPositions(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])

def subtractPositions(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])

def sol1(inputLines):
    charMap, positions = parseMap(inputLines)
    antennasByChar = defaultdict(list)

    for pos in positions:
        char = charMap[pos]
        if char == ".":
            continue
        antennasByChar[char].append(pos)

    anitNodes = set()

    for pos in positions:
        char = charMap[pos]
        if char == ".":
            continue

        for eqPos in antennasByChar[char]:
            if pos == eqPos:
                continue

            # Calculate difference
            res = subtractPositions(pos, eqPos)
            antiNodePos = addPositions(pos, res)

            # Check if within the bounds
            if antiNodePos in charMap:
                anitNodes.add(antiNodePos)

    return len(anitNodes)

with open(filePath, "r") as file:
    data = file.read().splitlines()

res = sol1(data)

print(res)