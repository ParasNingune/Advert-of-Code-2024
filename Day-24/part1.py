def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    # Parse initial wire values
    wire_values = {}
    gates = []
    for line in lines:
        if ':' in line:
            wire, value = line.split(': ')
            wire_values[wire] = int(value)
        elif '->' in line:
            gates.append(line)

    return wire_values, gates

def evaluate_gates(wire_values, gates):
    # Process each gate
    while gates:
        remaining_gates = []

        for gate in gates:
            parts = gate.split(' ')
            if len(parts) == 5:  # Format: input1 OP input2 -> output
                input1, op, input2, _, output = parts
                val1 = wire_values.get(input1)
                val2 = wire_values.get(input2)

                if val1 is not None and val2 is not None:
                    if op == 'AND':
                        wire_values[output] = val1 & val2
                    elif op == 'OR':
                        wire_values[output] = val1 | val2
                    elif op == 'XOR':
                        wire_values[output] = val1 ^ val2
                else:
                    remaining_gates.append(gate)

        gates = remaining_gates

    return wire_values

def calculate_output(wire_values):
    z_values = {k: v for k, v in wire_values.items() if k.startswith('z')}
    sorted_z = [v for k, v in sorted(z_values.items())]

    # Combine bits into a binary number
    binary_number = ''.join(map(str, sorted_z[::-1]))  # Reverse for least significant bit first
    return int(binary_number, 2)


input_file = "input.txt"
wire_values, gates = parse_input(input_file)
wire_values = evaluate_gates(wire_values, gates)
result = calculate_output(wire_values)
print(result)



# Answer -> 58740594706150