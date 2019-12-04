#!/usr/bin/env python3

import sys

# Constants
ADD = 1
MLT = 2
END = 99


# Parse input
code_array = [int(x.strip()) for x in sys.stdin.read().split(",")]

# Modify input
code_array[1] = 12
code_array[2] = 2

# Set up a pointer for the current opcode position
pointer = 0

while True:
    if code_array[pointer] == END:
        break

    if code_array[pointer] == ADD:
        code_array[code_array[pointer + 3]] = (
            code_array[code_array[pointer + 1]] + code_array[code_array[pointer + 2]]
        )
    else:
        code_array[code_array[pointer + 3]] = (
            code_array[code_array[pointer + 1]] * code_array[code_array[pointer + 2]]
        )

    pointer += 4

# Print result
print(code_array[0])
