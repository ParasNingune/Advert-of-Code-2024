filePath = "input.txt"

with open(filePath, "r") as file:
    data = file.read().strip()

lengths = list(map(int, data))

# Constructing disk array
disk = []
fileId = 0

for i, length in enumerate(lengths):
    disk.extend([fileId] * length if i%2 == 0 else ['.']*length)

    # Increment the fileId
    if i%2 ==0:
        fileId += 1

# Compact the disk. ie move blocks to fille gaps
left = 0
right = len(disk) - 1

while left < right:
    # Find leftmost gap
    while left < len(disk) and disk[left] != '.':
        left += 1

    # Find rightmose gap
    while right > left and disk[right] == '.':
        right -= 1

    if left < right:
        disk[left], disk[right] = disk[right], "."

# Calculate the checksum
checksum = sum(i * block for i, block in enumerate(disk) if block != '.')
print(checksum)


# Answer -> 6461289671426