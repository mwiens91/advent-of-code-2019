#!/usr/bin/env python3

import sys

# Constants
OPCODE_ADD = 1
OPCODE_MLT = 2
OPCODE_INP = 3
OPCODE_OUT = 4
OPCODE_JIT = 5
OPCODE_JIF = 6
OPCODE_ELT = 7
OPCODE_EEQ = 8
OPCODE_END = 9
MODE_POS = 0
MODE_IMM = 1
INPUT_DATA = 5


# Helper functions
def get_modes(expected_length, _chunk):
    chunk_len = len(_chunk)

    if chunk_len == 1:
        return [0] * (expected_length - 2)

    zeroes_to_add = expected_length - chunk_len

    return [0] * zeroes_to_add + _chunk[:-2]


# Parse input
code_array = [int(x.strip()) for x in sys.stdin.read().split(",")]

# Set up a pointer for the current position
pointer = 0

# Capture the output in an array
output = []

while True:
    # Parse the opcode
    chunk = [int(x) for x in str(code_array[pointer])]

    opcode = chunk[-1]

    # Handle no parameter opcodes
    if opcode == OPCODE_END:
        break

    # Handle one parameter opcodes
    if opcode in (OPCODE_INP, OPCODE_OUT):
        param_1 = code_array[pointer + 1]
        param_1_mode = get_modes(3, chunk)[0]

        if opcode == OPCODE_INP:
            code_array[param_1] = INPUT_DATA
        else:
            output.append(code_array[param_1] if param_1_mode == MODE_POS else param_1)

        pointer += 2
        continue

    # Handle two parameter opcodes
    if opcode in (OPCODE_JIT, OPCODE_JIF):
        param_1, param_2 = code_array[pointer + 1 : pointer + 3]
        param_2_mode, param_1_mode = get_modes(4, chunk)

        x = code_array[param_1] if param_1_mode == MODE_POS else param_1
        y = code_array[param_2] if param_2_mode == MODE_POS else param_2

        if (opcode == OPCODE_JIT and x != 0) or (opcode == OPCODE_JIF and x == 0):
            pointer = y
        else:
            pointer += 3

        continue

    # Handle three parameter opcodes
    param_1, param_2, param_3 = code_array[pointer + 1 : pointer + 4]
    _, param_2_mode, param_1_mode = get_modes(5, chunk)

    x = code_array[param_1] if param_1_mode == MODE_POS else param_1
    y = code_array[param_2] if param_2_mode == MODE_POS else param_2
    z = param_3

    if opcode == OPCODE_ADD:
        code_array[z] = x + y
    elif opcode == OPCODE_MLT:
        code_array[z] = x * y
    elif opcode == OPCODE_ELT:
        code_array[z] = 1 if x < y else 0
    else:
        code_array[z] = 1 if x == y else 0

    pointer += 4

# Print result
print(output[-1])
