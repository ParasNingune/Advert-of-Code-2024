noSafeDamped = 0
file_path = "input.txt"

def is_safe(report):

    # Check if the report is increasing or decreasing
    increasing = all(report[i] < report[i+1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i+1] for i in range(len(report) - 1))

    # Check if difference of adjacent pair in the report is less than 3
    difference = all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))

    return (increasing or decreasing) and difference

def is_safe_damp(report):
    if is_safe(report):
        return True
    
    # Check if removing any single level makes the report safe
    for i in range(len(report)):
        mod_report = report[:i] + report[i+1:]   # Removing the i-th level

        if is_safe(mod_report):
            return True
        
    return False    # Report cant be made safe

def count_safe_damped_states(file_path):
    with open(file_path, 'r') as inputFile:
        # Read each line as report, convert it to list of integers, and check if it is safe
        data = [list(map(int, line.split())) for line in inputFile.readlines()]

    # Count the no of safe reports
    return sum(is_safe_damp(report) for report in data)


# Count and print the no of Safe reports
noSafeDamped = count_safe_damped_states(file_path)
print(noSafeDamped)    

# Answer -> 634