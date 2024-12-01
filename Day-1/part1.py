leftDistance = []
rightDistance = []
totalDistance = 0

# Reading input
inputFile = open('input.txt', 'r')

# Spliting the input into left and right location
for each in inputFile:
    inputLine = each.split()
    leftDistance.append(inputLine[0])
    rightDistance.append(inputLine[1])

# Sorting both the list
leftDistance.sort()
rightDistance.sort()

# Subtracting both location and finding the distance
for i in range(0, len(leftDistance)):
    totalDistance += abs(int(leftDistance[i]) - int(rightDistance[i]))

# Printing final output
print(totalDistance)

# Answer -> 2086478