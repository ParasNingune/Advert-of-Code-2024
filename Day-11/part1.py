from collections import Counter, defaultdict
filePath = "input.txt"

with open(filePath, "r") as file:

    stones = list(map(int, file.read().split()))

initial_stones = Counter(stones)


def calculate(generations):
    stones_map = initial_stones

    for _ in range(generations):
        # Create a new map to store the updated stones after this generation.
        new_stones_map = defaultdict(int)

        # Iterate over each stone in the current stones_map.
        for s_nbr, n in stones_map.items():
            # If the stone is engraved with 0, replace it with a stone engraved with 1.
            if s_nbr == 0:
                new_stones_map[1] += n
            # If the stone has an even number of digits, split it into two stones.
            elif len(str(s_nbr)) % 2 == 0:
                s_nbr_str = str(s_nbr)
                middle = len(s_nbr_str) // 2
                new_stones_map[int(s_nbr_str[:middle])] += n
                new_stones_map[int(s_nbr_str[middle:])] += n
            # If the stone has an odd number of digits, replace it by multiplying it by 2024.
            else:
                new_stones_map[s_nbr * 2024] += n

        stones_map = new_stones_map

    return sum(stones_map.values())


print(calculate(25))

# Answer -> 217812