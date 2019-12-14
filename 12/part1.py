#!/usr/bin/env python3

import functools
import itertools
import re
import sys

# Parse input
lines = [line.strip() for line in sys.stdin]

num_moons = len(lines)
positions = [
    [int(x) for x in re.findall(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", line)[0]]
    for line in lines
]
velocities = [[0, 0, 0] for i in range(num_moons)]

# Run the simulation
N = 1000

for _ in range(N):
    # Apply gravity
    for m1, m2 in itertools.combinations(range(num_moons), 2):
        for x in range(3):
            if positions[m1][x] > positions[m2][x]:
                velocities[m1][x] -= 1
                velocities[m2][x] += 1
            elif positions[m1][x] < positions[m2][x]:
                velocities[m1][x] += 1
                velocities[m2][x] -= 1

    # Apply new position
    for m in range(num_moons):
        for x in range(3):
            positions[m][x] += velocities[m][x]

# Calculate energy
energy = functools.reduce(
    lambda e, m: e
    + sum([abs(x) for x in positions[m]]) * sum([abs(x) for x in velocities[m]]),
    range(num_moons),
    0,
)

print(energy)
