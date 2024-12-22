MOD = 16777216

def next_secret_number(secret):
    # --- Step 1 ---
    multiplied = secret * 64
    secret ^= multiplied
    secret %= MOD

    # --- Step 2 ---
    divided = secret // 32
    secret ^= divided
    secret %= MOD

    # --- Step 3 ---
    multiplied = secret * 2048
    secret ^= multiplied
    secret %= MOD

    return secret


def get_price_arrays(buyers):
    all_prices = []
    for initial_secret in buyers:
        secrets = [initial_secret]
        s = initial_secret
        # generate 2000 more
        for _ in range(2000):
            s = next_secret_number(s)
            secrets.append(s)
        prices = [x % 10 for x in secrets]  # last digit
        all_prices.append(prices)
    return all_prices


def solve_part_two(filename='input.txt'):
    buyers = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                buyers.append(int(line))

    # Get the 2001 prices for each buyer
    all_prices = get_price_arrays(buyers)

    from collections import defaultdict

    pattern_dict = defaultdict(lambda: [0]*len(buyers))

    for b_idx, prices in enumerate(all_prices):
        # Compute changes:
        changes = []
        for i in range(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            changes.append(diff)

        for i in range(len(changes) - 3):
            c1, c2, c3, c4 = changes[i], changes[i+1], changes[i+2], changes[i+3]
            pattern = (c1, c2, c3, c4)

            if pattern_dict[pattern][b_idx] == 0:
                sell_price = prices[i+4]
                pattern_dict[pattern][b_idx] = sell_price
    best_sum = 0
    for pattern, buyer_sells in pattern_dict.items():
        total_for_pattern = sum(buyer_sells)
        if total_for_pattern > best_sum:
            best_sum = total_for_pattern

    return best_sum


answer = solve_part_two("input.txt")
print(answer)

# Answer -> 2191