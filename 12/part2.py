#!/usr/bin/env python3

import itertools
import re
import sys
import numpy as np

# Parse input
lines = [line.strip() for line in sys.stdin]

num_moons = len(lines)
initial_positions = [
    [int(x) for x in re.findall(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", line)[0]]
    for line in lines
]

# Treat each coordinate separately
steps_until_repeat = []

for x in range(3):
    count = 0

    initial_x_positions = [m[x] for m in initial_positions]
    initial_x_velocities = [0] * num_moons

    x_positions = initial_x_positions.copy()
    x_velocities = initial_x_velocities.copy()

    while True:
        # Apply gravity
        for m1, m2 in itertools.combinations(range(num_moons), 2):
            if x_positions[m1] > x_positions[m2]:
                x_velocities[m1] -= 1
                x_velocities[m2] += 1
            elif x_positions[m1] < x_positions[m2]:
                x_velocities[m1] += 1
                x_velocities[m2] -= 1

        # Apply new position
        for m in range(num_moons):
            x_positions[m] += x_velocities[m]

        # Determine if we're done
        count += 1

        if x_positions == initial_x_positions and x_velocities == initial_x_velocities:
            break

    steps_until_repeat.append(count)

# Print answer
print(np.lcm.reduce(steps_until_repeat))
