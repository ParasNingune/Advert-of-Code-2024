def simulate_secret_numbers(secret, steps):
    MODULO = 16777216

    for _ in range(steps):
        # Step 1: Multiply by 64 and mix
        secret ^= (secret * 64) % MODULO
        secret %= MODULO

        # Step 2: Divide by 32 (integer division) and mix
        secret ^= (secret // 32) % MODULO
        secret %= MODULO

        # Step 3: Multiply by 2048 and mix
        secret ^= (secret * 2048) % MODULO
        secret %= MODULO

    return secret


# Read input from the file
with open("input.txt", "r") as file:
    initial_secrets = [int(line.strip()) for line in file if line.strip().isdigit()]

steps = 2000
total = 0

for secret in initial_secrets:
    total += simulate_secret_numbers(secret, steps)

print(total)

# Answer -> 20332089158