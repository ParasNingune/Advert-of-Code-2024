filePath = "input.txt"

# Read input from file
with open(filePath, "r") as file:
    data = file.read().splitlines()

def simulateProgram(registers, program):
    insPointer = 0
    output = []

    # Helper function to retrieve combo operand values
    def getCombo(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        else:
            raise ValueError("Invalid Combo Operand")

    # Simulate the program execution
    while insPointer < len(program):
        opcode = program[insPointer]
        operand = program[insPointer + 1]

        if opcode == 0:  # adv: Divide A by 2^operand
            denominator = 2 ** getCombo(operand)
            registers['A'] //= denominator

        elif opcode == 1:  # bxl: B XOR literal operand
            registers['B'] ^= operand

        elif opcode == 2:  # bst: Set B to combo operand % 8
            registers['B'] = getCombo(operand) % 8

        elif opcode == 3:  # jnz: Jump if A != 0
            if registers['A'] != 0:
                insPointer = operand
                continue  # Don't increment pointer after jump

        elif opcode == 4:  # bxc: B XOR C (operand ignored)
            registers['B'] ^= registers['C']

        elif opcode == 5:  # out: Output combo operand % 8
            output.append(getCombo(operand) % 8)

        elif opcode == 6:  # bdv: Divide A by 2^operand and store in B
            denominator = 2 ** getCombo(operand)
            registers['B'] = registers['A'] // denominator

        elif opcode == 7:  # cdv: Divide A by 2^operand and store in C
            denominator = 2 ** getCombo(operand)
            registers['C'] = registers['A'] // denominator

        else:
            raise ValueError("Invalid opcode")

        # Increment instruction pointer
        insPointer += 2

    # Return output as comma-separated string
    return ",".join(map(str, output))


# Parse input file
registerA = int(data[0].split(": ")[1])
registerB = int(data[1].split(": ")[1])
registerC = int(data[2].split(": ")[1])
program = list(map(int, data[4].split(": ")[1].split(",")))

# Initialize registers
registers = {"A": registerA, "B": registerB, "C": registerC}

# Simulate the program and print the result
res = simulateProgram(registers, program)
print(res)

# Answer -> 3,6,7,0,5,7,3,1,4