import re
filePath = "input.txt"

def calculateMultiplication(filePath):
    # Define the pattern to match valid multiplication instructions
    # The pattern matches `mul(X,Y)` where X and Y are numbers with 1-3 digits
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    try:
        with open(filePath, "r") as inputFile:
            memory = inputFile.read()
        
        # Use re.findall to find all matches for the defined pattern in the file content
        # Each match is a tuple of two strings representing the numbers    
        matches = re.findall(pattern, memory)

        # Calculate the total sum of products
        # Convert each pair of matched numbers to integers, multiply them, and sum up the results
        total = sum(int(x)*int(y) for x,y in matches)

        return total
    
    except FileNotFoundError:
        return None

result = calculateMultiplication(filePath)
print(result)

# Answer -> 189600467
