import itertools

def measure_performance(function):
    def wrapper(*args, **kwargs):
        
        result = function(*args, **kwargs)
        
        return result
    return wrapper


def read_input(file_path):
    with open(file_path, "r") as file:
        lock_data = [section.splitlines() for section in file.read().split("\n\n")]
    
    return [
        {(col, row) for col, line in enumerate(lock) 
                    for row, char in enumerate(line) if char == "#"} 
        for lock in lock_data
    ]


def solve_part_one(locks):
    no_overlap_pairs = 0
    for pattern_a, pattern_b in itertools.combinations(locks, 2):
        if not set.intersection(pattern_a, pattern_b):
            no_overlap_pairs += 1
    return no_overlap_pairs



lock_patterns = read_input("input.txt")
result = solve_part_one(lock_patterns)
print(result)

# Answer -> 2885