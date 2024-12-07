filePath = "input.txt"

with open(filePath, "r") as file:
    data = file.read()

# Splitting data into rules and updates
ruleSection, updateSection = data.strip().split("\n\n")

# Parse rules and updates
rules = [(int(x), int(y)) for x, y in (line.split("|") for line in ruleSection.splitlines())]
updates = [list(map(int, line.split(","))) for line in updateSection.splitlines()]

# Check if an update is correctly ordered
def updateOrder(update):
    index = {page: i for i, page in enumerate(update)}

    return all(index[x] < index[y] for x, y in rules if x in index and y in index)

middleSum = sum(update[len(update) // 2] for update in updates if updateOrder(update))
print(middleSum)

# Answer -> 4462