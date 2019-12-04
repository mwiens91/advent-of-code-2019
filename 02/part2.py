#!/usr/bin/env python3

from itertools import permutations
import sys

# Constants
ADD = 1
MLT = 2
END = 99
TARGET = 19690720

# Parse input
original_code_array = [int(x.strip()) for x in sys.stdin.read().split(",")]


def test(_code_array, noun, verb):
    # Create copy of original array
    code_array = _code_array.copy()

    # Modify input
    code_array[1] = noun
    code_array[2] = verb

    # Set up a pointer for the current opcode position
    pointer = 0

    while True:
        if code_array[pointer] == END:
            break

        if code_array[pointer] == ADD:
            code_array[code_array[pointer + 3]] = (
                code_array[code_array[pointer + 1]]
                + code_array[code_array[pointer + 2]]
            )
        else:
            code_array[code_array[pointer + 3]] = (
                code_array[code_array[pointer + 1]]
                * code_array[code_array[pointer + 2]]
            )

        pointer += 4

    # Return test result
    return bool(code_array[0] == TARGET)


for x, y in permutations(range(0, 100), 2):
    if test(original_code_array, x, y):
        print(100 * x + y)
        break
