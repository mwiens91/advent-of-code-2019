#!/usr/bin/env python3

import sys

# Constants
WIDTH = 25
HEIGHT = 6
SIZE = WIDTH * HEIGHT

# Parse input
raw_image = sys.stdin.read().strip()
num_layers = len(raw_image) // SIZE

# Check each layer
best_zero_count = SIZE
best_result = None

for i in range(0, num_layers):
    layer = raw_image[i * SIZE : (i + 1) * SIZE]

    if (best := layer.count("0")) < best_zero_count:
        best_zero_count = best
        best_result = layer.count("1") * layer.count("2")

print(best_result)
