#!/usr/bin/env python3

import sys

# Constants
WIDTH = 25
HEIGHT = 6
SIZE = WIDTH * HEIGHT

# Parse input
raw_image = sys.stdin.read().strip()
num_layers = len(raw_image) // SIZE

# Compute image
image = [2] * SIZE

for i in reversed(range(0, num_layers)):
    layer = raw_image[i * SIZE : (i + 1) * SIZE]

    for idx, val in enumerate(layer):
        if val != "2":
            image[idx] = val

# Convert image
converted_image = "\n".join(
    [
        "".join([" " if x == "0" else "█" for x in image[i * WIDTH : (i + 1) * WIDTH]])
        for i in range(HEIGHT)
    ]
)

print(converted_image)
