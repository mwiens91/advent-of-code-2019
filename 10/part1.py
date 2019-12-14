#!/usr/bin/env python3

import math
import sys

# Constants
ASTEROID = "#"
EMPTY = "."

# Parse input
lines = [line.strip() for line in sys.stdin]
points = []

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == ASTEROID:
            points.append((row, col))

# Calculate the best asteroid
best = 0

for parent in points:
    angles = set()

    for child in points:
        if child == parent:
            continue

        angle = math.atan2(parent[0] - child[0], parent[1] - child[1])

        if angle not in angles:
            angles.add(angle)

    best = max(best, len(angles))

print(best)
