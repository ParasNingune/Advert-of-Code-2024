from collections import Counter

leftLocation = []
rightLocation = []
totalSimilarityScore = 0

# Reading input
inputFile = open('input.txt', 'r')

# Spliting the input into left and right location
for each in inputFile:
    inputLine = each.split()
    leftLocation.append(inputLine[0])
    rightLocation.append(inputLine[1])

# Sorting both the list
leftLocation.sort()
rightLocation.sort()

# Counting occurrences of numbers in right list & Finding similarity scores
# Similartiy score = numberFromLeftList * occurrences(numberFromLeftList) in rightList
for lNum in leftLocation:
    similarity_score = 0
    for rNum in rightLocation:
        if int(rNum) == int(lNum):
            similarity_score += 1
    totalSimilarityScore += similarity_score * int(lNum)

print(totalSimilarityScore)

# Answer -> 24941624