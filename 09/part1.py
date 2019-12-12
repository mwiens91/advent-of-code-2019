#!/usr/bin/env python3

import sys


class IntcodeComputer:
    def __init__(self, first_input, second_input, code_array):
        self.inputs = [first_input, second_input]
        self.input_pointer = 0

        self.code_array = code_array
        self.code_pointer = 0

        self.relative_base = 0

        # Constants
        self.OPCODE_ADD = 1
        self.OPCODE_MLT = 2
        self.OPCODE_INP = 3
        self.OPCODE_OUT = 4
        self.OPCODE_JIT = 5
        self.OPCODE_JIF = 6
        self.OPCODE_ELT = 7
        self.OPCODE_EEQ = 8
        self.OPCODE_ADJ = 9
        self.OPCODE_END = 99
        self.MODE_POS = 0
        self.MODE_IMM = 1
        self.MODE_REL = 2

    def set_second_input(self, val):
        self.inputs[1] = val

    def get_modes(self, expected_length, _chunk):
        chunk_len = len(_chunk)

        if chunk_len == 1:
            return [self.MODE_POS] * (expected_length - 2)

        modes_to_add = expected_length - chunk_len

        return [self.MODE_POS] * modes_to_add + _chunk[:-2]

    def get_value_wrt_mode(self, val, mode):
        if mode == self.MODE_POS:
            return self.code_array[val]

        if mode == self.MODE_REL:
            return self.code_array[self.relative_base + val]

        return val

    def get_address_wrt_mode(self, addr, mode):
        if mode == self.MODE_REL:
            return self.relative_base + addr

        return addr

    def get_input(self):
        if self.input_pointer == 0:
            return self.inputs[self.input_pointer]

        self.input_pointer += 1
        return self.inputs[0]

    def get_output(self):
        while True:
            # Parse the opcode
            chunk = [int(x) for x in str(self.code_array[self.code_pointer])]

            opcode = chunk[-1]

            try:
                opcode_prefix = chunk[-2]
            except IndexError:
                opcode_prefix = 0

            # Handle no parameter opcodes
            if int("".join([str(opcode_prefix), str(opcode)])) == self.OPCODE_END:
                return None

            # Handle one parameter opcodes
            if opcode in (self.OPCODE_ADJ, self.OPCODE_INP, self.OPCODE_OUT):
                param_1 = self.code_array[self.code_pointer + 1]
                param_1_mode = self.get_modes(3, chunk)[0]

                x_val = self.get_value_wrt_mode(param_1, param_1_mode)
                x_addr = self.get_address_wrt_mode(param_1, param_1_mode)

                if opcode == self.OPCODE_OUT:
                    self.code_pointer += 2

                    return x_val

                if opcode == self.OPCODE_ADJ:
                    self.relative_base += x_val
                else:
                    self.code_array[x_addr] = self.get_input()

                self.code_pointer += 2

                continue

            # Handle two parameter opcodes
            if opcode in (self.OPCODE_JIT, self.OPCODE_JIF):
                param_1, param_2 = self.code_array[
                    self.code_pointer + 1 : self.code_pointer + 3
                ]
                param_2_mode, param_1_mode = self.get_modes(4, chunk)

                x = self.get_value_wrt_mode(param_1, param_1_mode)
                y = self.get_value_wrt_mode(param_2, param_2_mode)

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
            param_3_mode, param_2_mode, param_1_mode = self.get_modes(5, chunk)

            x = self.get_value_wrt_mode(param_1, param_1_mode)
            y = self.get_value_wrt_mode(param_2, param_2_mode)
            z = self.get_address_wrt_mode(param_3, param_3_mode)

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
input_code_array = [int(x.strip()) for x in sys.stdin.read().split(",")] + [0] * 100

# Compute the result
comp = IntcodeComputer(1, 1, input_code_array)
res = comp.get_output()

# Print result
print(res)
