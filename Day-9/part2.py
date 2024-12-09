filePath = "input.txt"

with open(filePath, "r") as file:
    lengths = list(map(int, file.read().strip()))

# Construct the disk array
disk = []
fileId = 0

for i, length in enumerate(lengths):
    disk.extend([fileId]*length if i%2 == 0 else ['.']*length)

    if i%2 ==0:
        fileId += 1

# Find suitable segment for a file
def findSegment(fileLength, maxIndex):
    count = 0

    for i in range(maxIndex):
        if disk[i] == ".":
            count += 1

            if count == fileLength:
                return i-count+1
        else:
            count = 0

    return None

# Move files to fill the gap
for fId in range(fileId-1, -1, -1):
    fPositions = [i for i, block in enumerate(disk) if block == fId]

    if not fPositions:
        continue

    fLength = len(fPositions)
    targetStart = findSegment(fLength, fPositions[0])

    if targetStart is not None:
        for pos in fPositions:
            disk[pos] = '.'
        for pos in range(targetStart, targetStart+fLength):
            disk[pos] = fId

# Calculate checksum
checksum = sum(i * block for i, block in enumerate(disk) if block != '.')
print(checksum)

# Answer -> 6488291456470