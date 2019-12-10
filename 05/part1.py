#!/usr/bin/env python3

import sys

# Constants
OPCODE_ADD = 1
OPCODE_MLT = 2
OPCODE_INP = 3
OPCODE_OUT = 4
OPCODE_END = 9
MODE_POS = 0
MODE_IMM = 1
INPUT_DATA = 1


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

    # Handle three parameter opcodes
    param_1, param_2, param_3 = code_array[pointer + 1 : pointer + 4]
    _, param_2_mode, param_1_mode = get_modes(5, chunk)

    x = code_array[param_1] if param_1_mode == MODE_POS else param_1
    y = code_array[param_2] if param_2_mode == MODE_POS else param_2

    if opcode == OPCODE_ADD:
        code_array[param_3] = x + y
    else:
        code_array[param_3] = x * y

    pointer += 4

# Print result
print(output[-1])
