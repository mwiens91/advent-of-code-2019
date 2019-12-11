#!/usr/bin/env python3

import itertools
import sys


class IntcodeComputer:
    def __init__(self, in1, in2, code_array):
        self.inputs = [in1, in2]
        self.input_pointer = 0
        self.code_array = code_array

        self.code_pointer = 0

        # Constants
        self.OPCODE_ADD = 1
        self.OPCODE_MLT = 2
        self.OPCODE_INP = 3
        self.OPCODE_OUT = 4
        self.OPCODE_JIT = 5
        self.OPCODE_JIF = 6
        self.OPCODE_ELT = 7
        self.OPCODE_EEQ = 8
        self.OPCODE_END = 9
        self.MODE_POS = 0
        self.MODE_IMM = 1

    def set_input_signal(self, sig):
        self.inputs[1] = sig

    def get_modes(self, expected_length, _chunk):
        chunk_len = len(_chunk)

        if chunk_len == 1:
            return [0] * (expected_length - 2)

        zeroes_to_add = expected_length - chunk_len

        return [0] * zeroes_to_add + _chunk[:-2]

    def get_input(self):
        if self.input_pointer:
            return self.inputs[self.input_pointer]

        self.input_pointer += 1
        return self.inputs[0]

    def get_output(self):
        while True:
            # Parse the opcode
            chunk = [int(x) for x in str(self.code_array[self.code_pointer])]

            opcode = chunk[-1]

            # Handle no parameter opcodes
            if opcode == self.OPCODE_END:
                return None

            # Handle one parameter opcodes
            if opcode in (self.OPCODE_INP, self.OPCODE_OUT):
                param_1 = self.code_array[self.code_pointer + 1]
                param_1_mode = self.get_modes(3, chunk)[0]

                if opcode == self.OPCODE_OUT:
                    self.code_pointer += 2

                    return (
                        self.code_array[param_1]
                        if param_1_mode == self.MODE_POS
                        else param_1
                    )

                self.code_array[param_1] = self.get_input()
                self.code_pointer += 2

                continue

            # Handle two parameter opcodes
            if opcode in (self.OPCODE_JIT, self.OPCODE_JIF):
                param_1, param_2 = self.code_array[
                    self.code_pointer + 1 : self.code_pointer + 3
                ]
                param_2_mode, param_1_mode = self.get_modes(4, chunk)

                x = (
                    self.code_array[param_1]
                    if param_1_mode == self.MODE_POS
                    else param_1
                )
                y = (
                    self.code_array[param_2]
                    if param_2_mode == self.MODE_POS
                    else param_2
                )

                if (opcode == self.OPCODE_JIT and x != 0) or (
                    opcode == self.OPCODE_JIF and x == 0
                ):
                    self.code_pointer = y
                else:
                    self.code_pointer += 3

                continue

            # Handle three parameter opcodes
            param_1, param_2, param_3 = self.code_array[
                self.code_pointer + 1 : self.code_pointer + 4
            ]
            _, param_2_mode, param_1_mode = self.get_modes(5, chunk)

            x = self.code_array[param_1] if param_1_mode == self.MODE_POS else param_1
            y = self.code_array[param_2] if param_2_mode == self.MODE_POS else param_2
            z = param_3

            if opcode == self.OPCODE_ADD:
                self.code_array[z] = x + y
            elif opcode == self.OPCODE_MLT:
                self.code_array[z] = x * y
            elif opcode == self.OPCODE_ELT:
                self.code_array[z] = 1 if x < y else 0
            else:
                self.code_array[z] = 1 if x == y else 0

            self.code_pointer += 4


# Parse input
original_code_array = [int(x.strip()) for x in sys.stdin.read().split(",")]

# Compute result
best = 0

for perm in itertools.permutations(range(5, 10)):
    current_input = 0
    comps = [IntcodeComputer(val, None, original_code_array.copy()) for val in perm]

    last_E_output = None
    halted = False

    while True:
        for comp in comps:
            comp.set_input_signal(current_input)
            output = comp.get_output()

            if output is None:
                halted = True
                break

            if comp == comps[-1]:
                last_E_output = output

            current_input = output

        if halted:
            break

    best = max(last_E_output, best)

# Print result
print(best)
